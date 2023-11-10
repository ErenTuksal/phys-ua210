import numpy as np
import scipy
import matplotlib.pyplot as plt
#defining brents method
def brent_min(func=None, astart=None, bstart=None, cstart=None, tol=1.e-5):
     
    
    grat = (3. - np.sqrt(5)) / 2
    a = astart
    b = bstart
    c = cstart
    while(np.abs(c - a) > tol):
        
        if((b - a) > (c - b)):
            x = b
            b = b - grat * (b - a)
        else:
            x = b + grat * (c - b)
        
        fb = func(b)
        fx = func(x)
        if(fb < fx):
            c = x
        else:
            a = b
            b = x 
    
    

    fa = func(a)
    fb = func(b)
    fc = func(c)
    denom = (b - a) * (fb - fc) - (b -c) * (fb - fa)
    numer = (b - a)**2 * (fb - fc) - (b -c)**2 * (fb - fa)
    
    if(np.abs(denom) < 1.e-15):
        x = b
    else:
        x = b - 0.5 * numer / denom
    return(x)


def f(x): 
    return ((x-0.3)**2)*np.exp(x)
#comparing our function vs scipy
print(brent_min(func=f, astart=0, bstart=0.25, cstart=0.5, tol=1.e-5))
print(scipy.optimize.brent(f))

