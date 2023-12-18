import numpy as np
import matplotlib.pyplot as plt
import banded

#We rescale L = 10^-8 to L = 1
L = 1
a = L/1000
h = 10**-4
times = np.arange(0, 0.25, h)
x = np.linspace(0, L, 1001)

#Following values are all scaled to L
x_init = L/2

sig = 10

kappa = 50


#Wave function
psi = np.exp(-1* ((x - x_init)**2)/(2*sig**2)) * np.exp(1j * kappa * x)



# Initializing a and b 
a1 = 1 + 1j*(h/(2*a**2))

a2 = -1j*(h/(4*a**2))

b1 = 1 - 1j*(h/(2*a**2))

b2 = 1j*(h/(4*a**2))


# Creating matrix A
N = 1001
A_diag = np.ones(N)*a1

A_upper_dia = np.ones(N) * a2
A_upper_dia[0] = 0
A_lower_dia = np.ones(N) * a2
A_lower_dia[-1] = 0

A = np.array([A_upper_dia, A_diag, A_lower_dia])




psi_val = []

for t in times:

    psi_val.append(psi)
    psi_0 = psi
    

    psi_0 = np.concatenate(([0],psi,[0])) 
    v = b1*psi_0[1:-1] + b2*(psi_0[2:]+psi_0[:-2])
    
 
    psi = banded.banded(A,v,1,1)
    psi[0] = psi[-1] = 0



psi_val = np.abs(np.array(psi_val))




plt.plot(x, psi_val[0])
plt.xlabel('Position (1e-8 m)')
plt.ylabel('Amplitude')
plt.title("At t = 0")
plt.savefig("init_psi.png")
plt.show()



plt.plot(x, psi_val[100])
plt.xlabel('Position (1e-8 m)')
plt.ylabel('Amplitude')

#Plot for t=0.0040
plt.plot(x, psi_val[500])
plt.xlabel('Position (1e-8 m)')
plt.ylabel('Amplitude')

plt.plot(x, psi_val[1000])
plt.xlabel('Position (1e-8 m)')
plt.ylabel('Amplitude')
plt.legend(["t= 0.001","t=0.005","t=0.01"])
plt.savefig("times_psi.png")

plt.show()
