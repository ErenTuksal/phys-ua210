import numpy as np
import matplotlib.pyplot as plt

#setting up f(x)
def f(x):
    
    return x**4 -2*x +1
# defining the integral
def trap_f(N,a,b):
    
    step = (b-a)/N
    
    s = 0.5*f(a)+ 0.5*f(b)
    
    for i in range(1,N):
        s += f(a+ (i*step))
    
        res = s*step
    return res


a = 0.0
b =2.0

# calculating integral with N = 10
I_1 = trap_f(10,a,b)
print(I_1)

I_2 = trap_f(20,a,b)

# printing percent error for calculated integral
print(abs(1 - (I_2/4.4)))

#printing calculated error
error = abs((1/3)*(I_2 - I_1))/4.4
print(error)
