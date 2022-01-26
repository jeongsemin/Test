import matplotlib.pyplot as plt
import librosa, librosa.display

y, sr = librosa.load(('C:/Users/user/Desktop/DigitalSound/F1.wav'))
mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=24)
fig, ax = plt.subplots()
img = librosa.display.specshow(mfccs, x_axis='time',ax=ax)
fig.colorbar(img, ax=ax)
ax.set(title='MFCC')
plt.show()