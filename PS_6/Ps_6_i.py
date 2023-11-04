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




c_index = (-eigen_vals).argsort()[::-1]
sorted_eig_vals = eigen_vals[c_index]
sorted_eig_vecs = eigen_vecs[c_index]



#Part i
#Now looking at first 20 components

N_c = 20
Pca = np.dot(residuals,sorted_eig_vecs[:, :N_c])
mean_grid = np.ones([9713,4001])
for i in range(len(mean_flux)):
    mean_grid[i] = mean_grid[i]*mean_flux[i]

Approx_spectra = np.dot(Pca, sorted_eig_vecs[:, :N_c].T) + mean_grid

plt.plot(logwave,Approx_spectra[1])
plt.plot(logwave,Approx_spectra[5])
plt.plot(logwave,Approx_spectra[10])
plt.plot(logwave,Approx_spectra[100])

plt.title("Approximate Spectra with N_c = 20")
plt.xlabel("Log(wavelength) in log(angstroms)")
plt.ylabel("Flux (10^−17 erg s^−1 cm^−2 A^−1)")
plt.savefig("Approx_spectra_Nc20")
plt.show()

#finding fractional residuals
residual_spectra = norm_flux - Approx_spectra

masked_norm_flux = np.ma.masked_values(norm_flux,0)

fractional_res = residual_spectra/masked_norm_flux

fract_res_squared = fractional_res*fractional_res

plt.plot(logwave,fract_res_squared[10])
plt.title("Fractional Residuas squared")
plt.xlabel("Log(wavelength) in log(angstroms)")
plt.ylabel("Fractional residuals squared")
plt.savefig("Fractonal_residuals_squared.png")
plt.show()

#looking at residuals closer

plt.plot(logwave,fract_res_squared[10])
plt.title("Fractional Residuas squared")
plt.xlabel("Log(wavelength) in log(angstroms)")
plt.ylabel("Fractional residuals squared")
plt.ylim([0,1.5])
plt.savefig("Fractonal_residuals_zoomed.png")
plt.show()



