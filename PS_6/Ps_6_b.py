
import numpy as np
import matplotlib.pyplot as plt
import astropy 

#Part a

from astropy.io import fits
hdu_list=astropy.io.fits.open("specgrid.fits")
logwave=hdu_list["LOGWAVE"].data 
flux=hdu_list["FLUX"].data



#part b
#finding normalization coefficent
coeffs = []

for i in range(len(flux)):
    coeff = np.sum(flux[i])
    coeffs.append(coeff)
    
coeffs = np.array(coeffs)
mult_coeffs= 1/coeffs

#multiplying flux with normalization coefficent
norm_flux = []

for k in range(len(flux)):
    norm_flux_elem = mult_coeffs[k]*flux[k]
    norm_flux.append(norm_flux_elem)
    
norm_flux = np.array(norm_flux)

#plotting normalized Galaxies

plt.plot(logwave,norm_flux[1])
plt.plot(logwave,norm_flux[5])
plt.plot(logwave,norm_flux[10])
plt.plot(logwave,norm_flux[100])
plt.title("Galaxies (normalized")
plt.xlabel("Log(wavelength) in log(angstroms)")
plt.ylabel("Flux (10^−17 erg s^−1 cm^−2 A^−1)")
plt.savefig("Galaxies_(normalized).png")
plt.show()
