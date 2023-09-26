import numpy as np
import matplotlib.pyplot as plt


N_Tl = 1000
tau_Tl = 3.053*60

mu = np.log(2)/tau_Tl

t = -1/mu*np.log(1-np.random.random(N_Tl))
t = np.sort(t)
decay = np.arange(1,N_Tl+1)
survive = N_Tl - decay

plt.plot(t, survive)
plt.plot(t, decay)
plt.xlabel ("Time (s)")
plt.ylabel("Number of atoms")
plt.legend(["Tl","Pb"])
plt.savefig("Problem_4Decay")
plt.show()
