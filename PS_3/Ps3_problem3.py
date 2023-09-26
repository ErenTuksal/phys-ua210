import numpy as np
import matplotlib.pyplot as plt
import random

#Creating initial number of atoms and list of the number of atoms per time for all elements

t_max = 20000
N_213Bi = 10000
step_s = 1
N_209Bi = 0
N_Pb = 0
N_Tl = 0
_213Bi_points = []
Pb_points = []
Tl_points =[]
_209Bi_points = []

#For loop over time

for t in np.arange(0,t_max,step_s):
    #Setting probabilities for elements
    tau_Pb = 3.3*60
    p_Pb = 1- 2**(-step_s/tau_Pb)
    tau_Tl = 2.2*60
    p_Tl = 1- 2**(-step_s/tau_Tl)
    tau_213Bi = 46*60
    p_Bi = 1- 2**(-step_s/tau_213Bi)
    p_Pb_Bi = p_Bi*0.9791
    p_Tl_Bi = p_Bi* 0.0209
    
    #Adding the number of elements at time t to the lists
    Pb_points.append(N_Pb)
    Tl_points.append(N_Tl)
    _209Bi_points.append(N_209Bi)
    _213Bi_points.append(N_213Bi)
    
    #Decay of Pb to 209Bi
    decay_pb = 0
    for i in range(N_Pb):
        if random.random() < p_Pb:
            decay_pb += 1
    
    N_Pb -= decay_pb
    N_209Bi += decay_pb

    #Decay of Tl to Pb
    decay_Tl = 0
    for i in range(N_Tl):
        if random.random()<p_Tl:
            decay_Tl +=1
                
    N_Tl -= decay_Tl
    N_Pb += decay_Tl
    
    #Decay of 213Bi into Pb and Tl
    decay_to_Pb = 0
    decay_to_Tl = 0
    for i in range(N_213Bi):
        
        if random.random() < p_Tl_Bi:
            decay_to_Tl +=1
        elif p_Tl_Bi<= random.random() < (p_Pb_Bi + p_Tl_Bi):
            decay_to_Pb +=1
                
    N_Pb += decay_to_Pb
    N_Tl += decay_to_Tl
    N_213Bi -= (decay_to_Pb+decay_to_Tl)
    
    
#Plotting    
plt.plot(_213Bi_points)
plt.plot(Pb_points)
plt.plot(Tl_points)
plt.plot(_209Bi_points)
plt.xlabel("Time (s)")
plt.ylabel("Number of atoms")
plt.legend(["213Bi","Pb","Tl","209Bi"])
plt.savefig("Problem3_Decay")
plt.show()    
