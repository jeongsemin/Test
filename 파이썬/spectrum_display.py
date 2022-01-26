import numpy as np
import librosa, librosa.display
from matplotlib import pyplot as plt

FIG_SIZE = (15,10)

file = "ahah.wav"
signal, sample_rate = librosa.load(file, sr=8000)


fft = np.fft.fft(signal)
print("fft shape : ",fft.shape)

spectrum = np.abs(fft)
print("spectrum shape : ", spectrum.shape)


f = np.linspace(0, sample_rate, len(spectrum))
print("f shape : ", f.shape)

left_spectrum = spectrum[:int(len(spectrum)/2)]
left_f = f[:int(len(spectrum)/2)]
print('left_spectrum shape : ', left_spectrum.shape)


print('left_f shape : ', left_f.shape)

plt.figure(figsize=FIG_SIZE)
plt.plot(left_f, left_spectrum, alpha=0.4)
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.title("Power Spectrum")
plt.show()

