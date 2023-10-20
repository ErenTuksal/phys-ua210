
import numpy as np
import matplotlib.pyplot as plt
import scipy

# reading the data 
signal = open("Signal.dat", "r")

time = []
sig = []
# seperating out time and the signal
signal.readline()
for line in signal:
    data = str(line).strip().split("|")
    
    time.append(float(data[1]))
    sig.append(float(data[2]))
#plotting time vs signal   
plt.plot(time,sig,".")

plt.title("Signal vs Time")
plt.xlabel("time(s)")
plt.ylabel("Signal")
plt.savefig("Signal vs Time.png")
plt.show()
#scaling time logarithmically for further use
t = np.log(np.array(time.copy()))
out = np.array(sig.copy())
times = np.array(time.copy())



#trying to fit a 3rd order polynomual
A = np.zeros((len(t),4))

A[:, 0] = 1.
A[:, 1] = t 
A[:, 2] = t**2
A[:, 3] = t**3


(u, w, vt) = np.linalg.svd(A, full_matrices=False)

ainv = vt.transpose().dot(np.diag(1. / w)).dot(u.transpose())

c = ainv.dot(out)

ym = A.dot(c)

plt.plot(t, out, '.')
plt.plot(t, ym, '.')


plt.title("Fitting Data")
plt.xlabel("ln(time)")
plt.ylabel("Signal")
plt.savefig("Fitting_to_poly1.png")
plt.show()

residuals = ym - out

plt.plot(t,residuals,".")
plt.title("Residuals")
plt.xlabel("ln(time)")
plt.ylabel("Residuals")
plt.savefig("Fitting_to_poly1_residuals.png")
plt.show()



# Now fitting higher order polynomual

A = np.zeros((len(t),8))

A[:, 0] = 1.
A[:, 1] = t 
A[:, 2] = t**2
A[:, 3] = t**3
A[:, 4] = t**4
A[:, 5] = t**5
A[:, 6] = t**6
A[:, 7] = t**7


(u, w, vt) = np.linalg.svd(A, full_matrices=False)


ainv = vt.transpose().dot(np.diag(1. / w)).dot(u.transpose())

c = ainv.dot(out)

ym = A.dot(c) 

plt.plot(t, out, '.')
plt.plot(t, ym, '.')


plt.title("Fitting Data with higher order polynomual")
plt.xlabel("ln(time)")
plt.ylabel("Signal")
plt.savefig("Fitting_to_poly2.png")
plt.show()

#plotting residuals

residuals = ym - out

plt.plot(t,residuals,".")
plt.title("Residuals With higher order polynomual")
plt.xlabel("ln(time)")
plt.ylabel("Residuals")
plt.savefig("Fitting_to_poly2_residuals.png")
plt.show()



#first frequency
freq_1 = 1/(2*np.max(times))

#number of harmonics
N = 12


A = np.zeros((len(times),2*N+2))
A[:, 0] = 1
for i in range(1, N+1):
    A[:,2*i-1] = np.sin(i*2*np.pi *freq_1*times)
    
    A[:,2*i] = np.cos(i*2*np.pi*freq_1*times)

(u, w, vt) = np.linalg.svd(A, full_matrices=False)


w_inv =[]

for i in w:
    if i != 0:
        w_inv.append(1/i)
    else:
        w_inv.append(0)
        
w_inv = np.array(w_inv)

ainv = vt.transpose().dot(np.diag(w_inv)).dot(u.transpose())

c = ainv.dot(out)

ym = A.dot(c) 

plt.plot(times, out, '.')
plt.plot(times, ym, '.')


plt.title("Fitting Data with Sines and Cosines")
plt.xlabel("time")
plt.ylabel("Signal")
plt.savefig("Fitting_to_SinCos.png")
plt.show()

#now the residuals of the sine fitting

residuals = ym - out

plt.plot(times,residuals,".")
plt.title("Residuals Sine")
plt.xlabel("time")
plt.ylabel("Residuals")
plt.savefig("Fitting_to_SinCos_residuals.png")
plt.show()

