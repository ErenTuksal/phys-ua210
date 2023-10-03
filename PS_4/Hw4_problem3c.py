import numpy as np
import matplotlib.pyplot as plt
from numpy import math

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



#Part c

#define modified integrand
def f_int(n,x):
    return ((x/(1-x**2))**2)*(1+x**2)/((1-x**2)**2)*abs(psi(n,(x/(1-x**2))))**2

#perform gaussian quadrature
N = 100
a = -1
b = 1
n = 5
z,w = np.polynomial.legendre.leggauss(N)
s = 0
for i in range(N):
    s += w[i]*f_int(n,z[i])
print(round(np.sqrt(s),9))
