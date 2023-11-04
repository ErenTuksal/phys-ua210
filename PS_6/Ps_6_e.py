
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



#Part e


#Now finding the Eigenvalues with the SVD decomposition
(u, w, vt) = np.linalg.svd(Covariance, full_matrices=False)

v = vt.transpose()

plt.plot(v[1])
plt.plot(v[2])
plt.plot(v[3])
plt.plot(v[4])
plt.plot(v[5])
plt.title(" First five rows of V from SVD")
plt.legend(["first","second","third","fourth","fifth"])
plt.savefig("First_five_rows_of_V_from_SVD.png")
plt.show()
