import numpy as np
from numpy import math
import matplotlib.pyplot as plt
import scipy

#Part a)
#defining hermite polynomual
def H(n,x):
    
    
    if n==0:
        return 1
    elif n==1:
        return 2*x
    else:
        return 2*x*H(n-1,x)-2 *(n-1)*H(n-2,x)

#definig the wave function psi_n(x)
def psi(n,x):
    
    ans = (1/np.sqrt((2**n)*math.factorial(n)*np.sqrt(np.pi))*np.exp((-x**2)/2))*H(n,x)
    
    return ans

#graphing psi_n(x) for n=1 to n = 3
x_vals = np.arange(-4,5,0.001)

for n in range(4):
    psi_vals = psi(n,x_vals)
    plt.plot(x_vals,psi_vals)

plt.title("Quantum Harmonic Oscillator Wave Functions")    
plt.xlabel("x")
plt.ylabel("Psi_n(x)")
plt.legend(["n = 0","n = 1","n = 2","n = 3"])
plt.savefig("quantum_osscilator_part_a")
plt.show()


