import numpy as np

# Function to multiply two NxN matrices A and B
def mat_mult(A = None,B = None,N=None):
    
    C = np.zeros([N,N],dtype = float)
    
    for i in range(N):
        for j in range(N):
            for k in range(N):
                C[i,j] += A[i,k]*B[k,j]
                
                
    return C

import time
import matplotlib.pyplot as plt
times_lst = []

#Timing the function for N = 10 to 200
for N in range(0,201,10):

    A = np.ones([N,N])
    B = np.random.randint(10, size=(N, N))



    start = time.time()
    ans = mat_mult(A,B,N)
    end = time.time()
    tme =end - start
    if N != 0:
        
        times_lst.append(tme)
    
#Plotting N vs the cube root of the time
plt.plot(range(10,201,10),np.cbrt(times_lst))

plt.title("Times for Matrix multiplication")
plt.xlabel("cube root of time(s^(1/3))")
plt.ylabel("N for NxN matrix")
plt.savefig("Problem2_NvsTimes")
plt.show()


#Now timing dot function of numpy
times_lst = []
dot_lst = []
for N in range(10,201,10):

    
    
    start = time.time()
    dot_lst.append(np.dot(A,B))
    end = time.time()
    tme =end - start
    times_lst.append(tme)
    
    
plt.plot(range(10,201,10),times_lst)

plt.title("Times for Matrix multiplication")
plt.xlabel("Time(s)")
plt.ylabel("N for NxN matrix")
plt.savefig("Problem2_NvsTimes_dot")
plt.show()
