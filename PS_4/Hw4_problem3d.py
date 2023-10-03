import numpy as np
import matplotlib.pyplot as plt
from numpy import math
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



#Part d

#defining integrated function
def f_herm(n,x):
    return ((x**2)*psi(n,x)**2)/np.exp(-x**2)


N = 100
n = 5
x_h,w_h = scipy.special.roots_hermite(N,mu=False)

s = (w_h*f_herm(n,x_h)).sum()
    
print(round(np.sqrt(s),9))
