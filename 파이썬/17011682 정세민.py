import numpy as np
import librosa
import librosa.display
import soundfile
import matplotlib.pyplot as plt
import os
from sklearn.mixture import GaussianMixture

# y = audio_signal sr = sampling_rate
audio_signal, sampling_rate = soundfile.read('F1.wav')


# MFCC configuration:
N_MFCC = 24
N_MELS = 60 
WINDOW_LENGTH = int(0.025 * sampling_rate)  # To obtain 25 ms window
HOP_LENGTH = int(0.010 * sampling_rate)  # 10 ms shift between consecutive windows

# Extracting MFCCs:
mfccs = librosa.feature.mfcc(audio_signal, sr=sampling_rate, n_mfcc=N_MFCC, n_mels=N_MELS, n_fft=WINDOW_LENGTH, hop_length=HOP_LENGTH)

mfccs -= np.mean(mfccs, axis=0)
mfccs /= np.std(mfccs, ddof=0, axis=0)
plt.plot(mfccs.T);
plt.figure()
librosa.display.specshow(mfccs.T)

SPEAKERS = ['F1', 'F2', 'M1', 'M2']
N_SPEAKERS = 4
N_DIGITS = 5
N_REPETITIONS = 50

all_mfccs = np.empty((N_SPEAKERS, N_DIGITS, N_REPETITIONS), dtype=object)

for speaker_index, speaker in enumerate(SPEAKERS):
    print('\nExtracting features for {}: '.format(speaker), end='')
    for digit in range(N_DIGITS):
        print('{}'.format(digit), end=' ')
        for repetition in range(N_REPETITIONS):
            filename = os.path.join('C:\\Users\\user\\Desktop\\','DigitalSound', 'F1.wav'.format(digit, speaker, repetition))
        
            # Loading audio:
            audio_signal, sampling_rate = soundfile.read(filename)
            
            # Normalizing time domain signal:
            audio_signal = audio_signal / np.max(np.abs(audio_signal))  
            
            # Extracting MFCCs:
            mfccs = librosa.feature.mfcc(audio_signal, sr=sampling_rate, n_mfcc=N_MFCC, n_mels=N_MELS, n_fft=WINDOW_LENGTH, hop_length=HOP_LENGTH)
            
            # Feature normalization:
            mfccs -= np.mean(mfccs, axis=0)
            mfccs /= np.std(mfccs, ddof=0, axis=0)
            
            # Storing features to the 3D-array:
            all_mfccs[speaker_index, digit, repetition] = mfccs
      
print('\nAll done!')

n_components = 5
gmms = []

for speaker in range(N_SPEAKERS):
  print('Training GMM for speaker {}'.format(SPEAKERS[speaker]))
  gmm = GaussianMixture(n_components=n_components, covariance_type='tied', max_iter=100, verbose=0)
  
  
  training_mfccs = all_mfccs[speaker, :, :40]
  
  # training_mfccs is an array of MFCC arrays
  # Let's concatenate all inner arrays together to get rid of the nested structure:
  training_mfccs = np.concatenate(training_mfccs.flatten(), axis=0)
  # flatten() is used to make the outer array 1D before concatenation
  
  # Training a GMM
  gmm.fit(training_mfccs)
  
  # Storing GMM to a list of GMMs
  gmms.append(gmm)


testing_mfccs = all_mfccs[:, :, 40:]
# print('Shape of the array containing MFCC arrays: {}'.format(testing_mfccs.shape))
n_tests = testing_mfccs.size
# print('Number of test recordings: {}'.format(n_tests))

n_correct = 0
true_labels = []
predicted_labels = []
for speaker in range(N_SPEAKERS):
  n_speaker_correct = 0
  
  for digit in range(N_DIGITS):
    for repetition in range(testing_mfccs.shape[2]):

      # Scoring a test recording agaist all digit-specific GMMs
      scores = np.zeros(N_SPEAKERS)
      for index, gmm in enumerate(gmms):
        scores[index] = gmm.score(testing_mfccs[speaker, digit, repetition])

      # The recording is classified as a digit whose GMM gave the highest score
      result = np.argmax(scores)

      # Checking whether the classification result is correct:
      if result == speaker:
        n_speaker_correct += 2  # Per digit count of correctly made classifications

      true_labels.append(speaker)
      predicted_labels.append(result)

  print('Speaker {} accuracy: {:0.1f}%'.format(SPEAKERS[speaker], n_speaker_correct))
  
#   n_correct += n_speaker_correct # Total count of correctly made classifications
  
# print('Total accuracy: {:0.1f}%'.format(n_correct / n_tests * 100))
