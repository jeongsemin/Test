import numpy as np
import librosa, librosa.display
from matplotlib import pyplot as plt

FIG_SIZE = (15,10)
file = "delme_rec_unlimited_i29hcnpt.wav"

signal, sample_rate = librosa.load(file, sr=44100)
print('signal shape : ', signal.shape)

plt.figure(figsize=FIG_SIZE)
librosa.display.waveplot(signal, sample_rate, alpha =0.4)
plt.xlabel("Time (sec)")
plt.ylabel("Amplitude")
plt.title("Waveform")
plt.show()
