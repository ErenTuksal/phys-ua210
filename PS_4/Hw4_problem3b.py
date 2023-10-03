
import numpy as np
from numpy import math
import matplotlib.pyplot as plt
import scipy


def H(n,x):
    
    
    if n==0:
        return 1
    elif n==1:
        return 2*x
    else:
        return 2*x*H(n-1,x)-2 *(n-1)*H(n-2,x)


def psi(n,x):
    
    ans = (1/np.sqrt((2**n)*math.factorial(n)*np.sqrt(np.pi))*np.exp((-x**2)/2))*H(n,x)
    
    return ans








#part b

new_x_vals = np.linspace(-10,10,1000)

psi_vals = psi(30,new_x_vals)

#plotting psi_n(x) with n = 30
plt.plot(new_x_vals,psi_vals)
plt.title("Quantum Harmonic Oscillator Wave Functions")    
plt.xlabel("x")
plt.ylabel("Psi_n(x)")
plt.legend(["n = 30"])
plt.savefig("quantum_osscilator_part_b")
plt.show()
