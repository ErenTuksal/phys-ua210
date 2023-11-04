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



#Part d
#Finding covariance matrix



Covariance = np.cov(residuals, rowvar =False)

#Now finding and plotting eigenvectors

(eigen_vals,eigen_vecs) = np.linalg.eig(Covariance)
#Plotting first five eigenvectors

plt.plot(eigen_vecs[1])
plt.plot(eigen_vecs[2])
plt.plot(eigen_vecs[3])
plt.plot(eigen_vecs[4])
plt.plot(eigen_vecs[5])
plt.title(" First five eigenvectors of the Covariance Matrix")
plt.legend(["first","second","third","fourth","fifth"])
plt.savefig("First_five_eigen.png")
plt.show()













