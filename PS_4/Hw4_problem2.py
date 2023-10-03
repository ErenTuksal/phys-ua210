import numpy as np
import matplotlib.pyplot as plt

# defining V(x) = x^4
def V(x):
    return x**4

# defining function to be integrated
def func(x,m,a):
    
    return np.sqrt(8*m)*(1/np.sqrt(V(a)-V(x)))
    

N=20
lower_bnd = 0
upper_bnd = 2
m = 1

#defining integral with gaussian quadrature
def gauss_int(N,lower_bnd,upper_bnd,m):
    x,W = x,w= np.polynomial.legendre.leggauss(N)

    xp=0.5*(upper_bnd-lower_bnd)*x + 0.5*(upper_bnd+lower_bnd) 
    wp=0.5*(upper_bnd-lower_bnd)*w

    s=0.0 
    for k in range(N): 
        s+=wp[k]*func(xp[k],m,upper_bnd)
    return s

# running integral with different upper bounds and graphing values
N=20
lower_bnd = 0
m = 1
val_lst = []
for upper_bnd in np.arange(0.01,2.01,0.01):
    val = gauss_int(N,lower_bnd,upper_bnd,m)
    
    val_lst.append(val)

plt.plot(np.arange(0.01,2.01,0.01),val_lst)
plt.title("Period for Amplitudes")
plt.xlabel("Amplitude (m)")
plt.ylabel("period (s)")
plt.savefig("Period_of_Harmonic_Osscilator.png")
plt.show()

