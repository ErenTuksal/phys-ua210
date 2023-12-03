import numpy as np
import scipy
import matplotlib.pyplot as plt
#loading piano data
piano = np.loadtxt("piano.txt")


#plotting piano against time
plt.plot(piano)
plt.xlabel("t")
plt.ylabel("magnitude")
plt.savefig("Piano.png")
plt.show()


#Finding the fourier transform and plotting it
Ts = 1/44100


fftsignal = scipy.fft.fft(piano)[:10000]

freq_range = scipy.fft.fftfreq(len(piano), Ts)[:10000]

plt.plot(freq_range,abs(fftsignal))

plt.ylabel("Magnitude")
plt.xlabel("Frequency")
plt.savefig("Piano_fft.png")
plt.show()


#loading trumpet data

trumpet = np.loadtxt("trumpet.txt")

#plotting trumpet vs time
plt.plot(trumpet)

plt.xlabel("t")
plt.ylabel("magnitude")
plt.savefig("trumpet.png")
plt.show()


#taking the fourier transform for the trumpet




fftsignal = scipy.fft.fft(trumpet)[:10000]

freq_range = scipy.fft.fftfreq(len(trumpet), Ts)[:10000]

plt.plot(freq_range,abs(fftsignal))

plt.ylabel("Magnitude")
plt.xlabel("Frequency")
plt.savefig("trumpet_fft.png")
plt.show()





