import numpy as np
import matplotlib.pyplot as plt

#defining equations
def f(r,t):
    sig = 10
    r_c = 28
    b = 8/3
    x = r[0]
    y = r[1]
    z = r[2]
    fx = sig*(y-x)
    fy = r_c*x-y-x*z
    fz = x*y-b*z
    return np.array([fx,fy,fz])

#creating the grid and timestep
dt = 50/10000
t_grid = np.arange(0,50,dt)
x_grid = []
y_grid = []
z_grid = []

#initial condition
r = np.array([0.0,1.0,0.0])

#iterating 
for t in t_grid:
    
    
    x_grid.append(r[0])
    y_grid.append(r[1])
    z_grid.append(r[2])
    u1 = dt*f(r,t)
    u2 = dt*f(r+0.5*u1,t+0.5*dt)
    u3 = dt*f(r+0.5*u2,t+0.5*dt)
    u4 = dt*f(r+u3,t+dt)
    r += (u1+2*u2+2*u3+u4)/6


plt.plot(t_grid,y_grid)
plt.xlabel("time")
plt.ylabel("y")
plt.savefig("ty_plot.png")
plt.show()

plt.plot(x_grid,z_grid)
plt.xlabel("x")
plt.ylabel("z")
plt.savefig("xz_plot.png")
plt.show()
