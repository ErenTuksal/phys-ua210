



import numpy as np
import matplotlib.pyplot as plt
import astropy 



from astropy.io import fits
hdu_list=astropy.io.fits.open("specgrid.fits")
logwave=hdu_list["LOGWAVE"].data 
flux=hdu_list["FLUX"].data


coeffs = []

for i in range(len(flux)):
    coeff = np.sum(flux[i])
    coeffs.append(coeff)
    
coeffs = np.array(coeffs)
mult_coeffs= 1/coeffs


norm_flux = []

for k in range(len(flux)):
    norm_flux_elem = mult_coeffs[k]*flux[k]
    norm_flux.append(norm_flux_elem)
    
norm_flux = np.array(norm_flux)





mean_flux = []

for j in range(len(norm_flux)):
    mean = np.sum(norm_flux[j])/len(norm_flux[j])
    mean_flux.append(mean)
len(mean_flux)

mean_flux = np.array(mean_flux)


residuals = []
for x in range(len(norm_flux)):
    
    residual_flux = norm_flux[x]-mean_flux[x]
    residuals.append(residual_flux)
    
residuals = np.array(residuals)







Covariance = np.cov(residuals, rowvar =False)



(eigen_vals,eigen_vecs) = np.linalg.eig(Covariance)

#Part g

#Finding first five principal components
c_index = (-eigen_vals).argsort()[::-1]
sorted_eig_vals = eigen_vals[c_index]
sorted_eig_vecs = eigen_vecs[c_index]

N_c = 5
Pca = np.dot(residuals,sorted_eig_vecs[:, :N_c])
mean_grid = np.ones([9713,4001])
for i in range(len(mean_flux)):
    mean_grid[i] = mean_grid[i]*mean_flux[i]

Approx_spectra = np.dot(Pca, sorted_eig_vecs[:, :N_c].T) + mean_grid


plt.plot(logwave,Approx_spectra[1])
plt.plot(logwave,Approx_spectra[5])
plt.plot(logwave,Approx_spectra[10])
plt.plot(logwave,Approx_spectra[100])

plt.title("Approximate Spectra with N_c = 5")
plt.xlabel("Log(wavelength) in log(angstroms)")
plt.ylabel("Flux (10^−17 erg s^−1 cm^−2 A^−1)")
plt.savefig("Approximate_Spectra_with_N_c_5.png")
plt.show()
