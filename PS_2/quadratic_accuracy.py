import numpy as np

def quad_solver_1(a,b,c):
    sol_lst = []
    
    x_1 = (-b + np.sqrt(b**2-(4*a*c)))/(2*a)
    
    x_2 = (-b - np.sqrt(b**2-(4*a*c)))/(2*a)
    
    sol_lst.append(x_1)
    sol_lst.append(x_2)
    
    solutions = np.array(sol_lst)
    
    print(solutions)

quad_solver_1(0.001,1000,0.001)

#now with second version of quadratic equation

def quad_solver_2(a,b,c):
    sol_lst = []
    alt_sol_lst =[]
    
   
    
    x_1_alt = 2*c/(-b - np.sqrt(b**2 - 4*a*c))
    
    x_2_alt = 2*c/(-b - np.sqrt(b**2 - 4*a*c))
    
  
    
    alt_sol_lst.append(x_1_alt)
    alt_sol_lst.append(x_2_alt)
    
    alt_sols = np.array(alt_sol_lst)

    
    print(alt_sols)

quad_solver_2(0.001,1000,0.001)

#accurate version

def quad_solver_acc(a,b,c):
    sol_lst = []
    a = np.float64(a)
    b = np.float64(b)
    c = np.float64(c)
    x_1 = (-b + np.sqrt(b**2-(4*a*c)))/(2*a)
    
    x_2 = (-b - np.sqrt(b**2-(4*a*c)))/(2*a)
    
    sol_lst.append(x_1)
    sol_lst.append(x_2)
    
    solutions = np.array(sol_lst)
    
    print(solutions)
quad_solver_acc(0.001,1000,0.001)

