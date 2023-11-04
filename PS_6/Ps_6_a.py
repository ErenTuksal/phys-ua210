
import numpy as np
import matplotlib.pyplot as plt
import astropy 

#Part a

from astropy.io import fits
hdu_list=astropy.io.fits.open("specgrid.fits")
logwave=hdu_list["LOGWAVE"].data 
flux=hdu_list["FLUX"].data



#plotting galaxies
plt.plot(logwave,flux[1])
plt.plot(logwave,flux[5])
plt.plot(logwave,flux[10])
plt.plot(logwave,flux[100])
plt.title("Galaxies")
plt.xlabel("Log(wavelength) in log(angstroms)")
plt.ylabel("Flux (10^−17 erg s^−1 cm^−2 A^−1)")
plt.savefig("Galaxies.png")
plt.show()



