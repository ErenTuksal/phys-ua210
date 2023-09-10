import numpy as np
import matplotlib.pyplot as plt
def gaussian_pdf(x,mean,std_dev):
    gaussian = (1/(float(std_dev)*np.sqrt(2*np.pi)))*np.exp(-0.5*((x-mean)/std_dev)**2)
    return gaussian
x = np.linspace(-10,10,10000)
mean = 0
std_dev = 3
plt.plot(x,gaussian_pdf(x,mean,std_dev),)
plt.show
plt.savefig("gaussian.png")
