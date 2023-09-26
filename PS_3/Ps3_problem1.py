import numpy as np
#The function
def f(x=None,dtype = float):  
    return x*(x-1)
#The analytical derivative
def fp_analytic(x=None,dtype = float):
    return 2*x -1

#Numerical Derivative

def fp_num(x = None,delta= None,dtype = float):
    return (f((x+delta))-f(x))/delta


#Test with delta = 10^-2
print(fp_analytic(1))
print(fp_num(1,10**-2))

#Furher tests with delta = 10^-4,10^-6,...,10^-14

print(fp_num(1,10**-4))
print(fp_num(1,10**-6))
print(fp_num(1,10**-8))
print(fp_num(1,10**-10))
print(fp_num(1,10**-12))
print(fp_num(1,10**-14))
