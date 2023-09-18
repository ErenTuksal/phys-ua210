import numpy as np
import matplotlib.pyplot as plt

def calculate_M1(L):
    M = 0
    for i in range(-L,L+1):
        for j in range(-L,L+1):
            for k in range(-L,L+1):

                if (i==j==k==0):
                    continue

                M += (-1)**(i+j+k)/(np.sqrt(i**2+j**2+k**2))
                
    print("Magelung constant is",round(M,4))

calculate_M1(L=100)

#Without for loops:

def calculate_M2(L_2):
    
    r = np.math.floor(L_2 ** (1 / 3)/2)
    
    i = np.arange(-r, r+1)
    j = np.arange(-r, r+1)
    k = np.arange(-r, r+1)
    i, j, k = np.meshgrid(i,j,k)


    mask = (i != 0) | (j != 0) | (k != 0)

    distance = np.sqrt(i**2 + j**2 + k**2)
    sign = (-1.0) ** (i + j + k)

    
    M = np.sum(sign[mask] / distance[mask])

    print("Magelung constant is",round(M,4))


calculate_M2(L_2=100)
