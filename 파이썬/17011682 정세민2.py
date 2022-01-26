import os
import librosa
import librosa.display
import soundfile
import matplotlib.pyplot as plt
from sklearn.mixture import GaussianMixture

# N_MFCC = 24 , 16000HZ
N_MFCC = 24    
sr = 16000

# 파일 불러오기
# F1
filename = os.path.join('C:\\Users\\user\\Desktop\\','DigitalSound', 'F1.wav')
y1, sr = soundfile.read(os.path.join(filename))
F1 =  librosa.feature.mfcc(y=y1, sr=sr, n_mfcc=N_MFCC, hop_length = 512 + 1).T
# F2
filename2 = os.path.join('C:\\Users\\user\\Desktop\\','DigitalSound', 'F2.wav')
y2, sr = soundfile.read(os.path.join(filename2))
F2 =  librosa.feature.mfcc(y=y2, sr=sr, n_mfcc=N_MFCC, hop_length = 512 + 1).T
# F3
filename3 = os.path.join('C:\\Users\\user\\Desktop\\','DigitalSound', 'M1.wav')
y3, sr = soundfile.read(os.path.join(filename3))
M1 =  librosa.feature.mfcc(y=y3, sr=sr, n_mfcc=N_MFCC, hop_length = 512 + 1).T
# F4
filename4 = os.path.join('C:\\Users\\user\\Desktop\\','DigitalSound', 'M2.wav')
y4, sr = soundfile.read(os.path.join(filename4))
M2 =  librosa.feature.mfcc(y=y4, sr=sr, n_mfcc=N_MFCC, hop_length = 512 + 1).T

# Normalization
import numpy as np

F1 -= np.mean(F1, axis=0)
F1 /= np.std(F1, ddof=0, axis=0)

F2 -= np.mean(F2, axis=0)
F2 /= np.std(F2, ddof=0, axis=0)

M1 -= np.mean(M1, axis=0)
M1 /= np.std(M1, ddof=0, axis=0)

M2 -= np.mean(M2, axis=0)
M2 /= np.std(M2, ddof=0, axis=0)

# 참고
# n_components = 5
# gmms = []

# for speaker in range(N_SPEAKERS):
#   print('Training GMM for speaker {}'.format(SPEAKERS[speaker]))
#   gmm = GaussianMixture(n_components=n_components, covariance_type='tied', max_iter=100, verbose=0)
  
  
#   training_mfccs = all_mfccs[speaker, :, :40]
  
#   # training_mfccs is an array of MFCC arrays
#   # Let's concatenate all inner arrays together to get rid of the nested structure:
#   training_mfccs = np.concatenate(training_mfccs.flatten(), axis=0)
#   # flatten() is used to make the outer array 1D before concatenation
  
#   # Training a GMM
#   gmm.fit(training_mfccs)
  
#   # Storing GMM to a list of GMMs
#   gmms.append(gmm)

n_components = 5
gmms = []

# Training a GMM
mfccs = [F1, F2, M1, M2]
for mfcc in mfccs:
    gmm = GaussianMixture(n_components=n_components, covariance_type='tied', max_iter=200, verbose=0)
    gmm.fit(mfcc)
    gmms.append(gmm)
    
i = 130000 
time = 25600 # 16000 * 1.6

def test_data(i): # 0 ~ 256000 - 25600(1.6sec)
    _y1 = y1[i:i+time]
    _y2 = y2[i:i+time]
    _y3 = y3[i:i+time]
    _y4 = y4[i:i+time]

    _F1 = librosa.feature.mfcc(y=_y1, sr=sr, n_mfcc=24, hop_length = 512 + 1).T
    _F2 = librosa.feature.mfcc(y=_y2, sr=sr, n_mfcc=24, hop_length = 512 + 1).T
    _F3 = librosa.feature.mfcc(y=_y3, sr=sr, n_mfcc=24, hop_length = 512 + 1).T
    _F4 = librosa.feature.mfcc(y=_y4, sr=sr, n_mfcc=24, hop_length = 512 + 1).T

    _F1 -= np.mean(_F1, axis=0)
    _F1 /= np.std(_F1, ddof=0, axis=0)
    _F2 -= np.mean(_F2, axis=0)
    _F2 /= np.std(_F2, ddof=0, axis=0)
    _F3 -= np.mean(_F3, axis=0)
    _F3 /= np.std(_F3, ddof=0, axis=0)
    _F4 -= np.mean(_F4, axis=0)
    _F4 /= np.std(_F4, ddof=0, axis=0)
    
    return _F1, _F2, _F3, _F4

SPEACKER = {0:"F1", 1:"F2", 2:"M1", 3:"M2"}

Data = []


for i in range(70000, 256000-25600 +1, 100):
    v1,v2,v3,v4 = test_data(i)
    Data.append((v1,v2,v3,v4))


for j, k in enumerate(Data):
    for i, h in enumerate(k):
        scores = []
        for index, gmm in enumerate(gmms):
            scores.append(gmm.score(h))

#         print(i, np.argmax(scores))
        if(i == np.argmax(scores)) :
#             print("True")
            pass
        else:
            print(j, "False")
            


# 테스트 실행
test_file1 = 'C:\\Users\\user0425\\Desktop\\DigitalSound\\1.wav'
test_file2 = 'C:\\Users\\user0425\\Desktop\\DigitalSound\\2.wav'
test_file3 = 'C:\\Users\\user0425\\Desktop\\DigitalSound\\3.wav'
test_file4 = 'C:\\Users\\user0425\\Desktop\\DigitalSound\\4.wav'
test_file5 = 'C:\\Users\\user0425\\Desktop\\DigitalSound\\5.wav'


# 똑같이 MFCC추출 및 GMM학습
Y1, sr = soundfile.read(test_file1)
TEST_F1 =  librosa.feature.mfcc(y=Y1, sr=sr, n_mfcc=24, hop_length = 512 + 1).T

Y2, sr = soundfile.read(test_file2)
TEST_F2 =  librosa.feature.mfcc(y=Y2, sr=sr, n_mfcc=24, hop_length = 512 + 1).T

Y3, sr = soundfile.read(test_file3)
TEST_F3 =  librosa.feature.mfcc(y=Y3, sr=sr, n_mfcc=24, hop_length = 512 + 1).T

Y4, sr = soundfile.read(test_file4)
TEST_F4 =  librosa.feature.mfcc(y=Y4, sr=sr, n_mfcc=24, hop_length = 512 + 1).T

Y5, sr = soundfile.read(test_file5)
TEST_F5 =  librosa.feature.mfcc(y=Y5, sr=sr, n_mfcc=24, hop_length = 512 + 1).T


TEST_F1 -= np.mean(TEST_F1, axis=0)
TEST_F1 /= np.std(TEST_F1, ddof=0, axis=0)

TEST_F2 -= np.mean(TEST_F2, axis=0)
TEST_F2 /= np.std(TEST_F2, ddof=0, axis=0)

TEST_F3 -= np.mean(TEST_F3, axis=0)
TEST_F3 /= np.std(TEST_F3, ddof=0, axis=0)

TEST_F4 -= np.mean(TEST_F4, axis=0)
TEST_F4 /= np.std(TEST_F4, ddof=0, axis=0)

TEST_F5 -= np.mean(TEST_F5, axis=0)
TEST_F5 /= np.std(TEST_F5, ddof=0, axis=0)

# 파일 열기
f = open("result.txt", 'a')

TEST_MFCC = [TEST_F1, TEST_F2, TEST_F3, TEST_F4, TEST_F5]

SPEACKER = {0:"F1", 1:"F2", 2:"M1", 3:"M2"}
for test_mfcc in TEST_MFCC:
    scores =[]
    for index, gmm in enumerate(gmms):
        scores.append(gmm.score(test_mfcc))

    print(SPEACKER[np.argmax(scores)])
    f.write(SPEACKER[np.argmax(scores)] + '\n')

# 파일 닫기
f.close() 