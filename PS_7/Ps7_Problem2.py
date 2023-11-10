


import numpy as np
import scipy
import matplotlib.pyplot as plt



age = np.array(np.loadtxt("survey.csv",skiprows=1,usecols=0,delimiter=","))
answer = np.array(np.loadtxt("survey.csv",skiprows=1,usecols=1,delimiter=","))


def p(x,bet0,bet1):
    return 1/(1+np.exp(-(bet0+bet1*x)))






def neg_log_like(beta,x,res):
    bet0 = beta[0] 
    bet1 = beta[1] 
    
    val_lst = []
    for i in range(len(x)):
        elem = res[i]*np.log(p(x[i],bet0,bet1)/(1-p(x[i],bet0,bet1)))+np.log(1-p(x[i],bet0,bet1))
        val_lst.append(elem)
    return  -np.sum(np.array(val_lst))
    



beta = np.array([0.1,0.1])

result = scipy.optimize.minimize(lambda beta, age, answer: neg_log_like(beta, age, answer), beta,  args=(age,answer))

covariance = result.hess_inv*result.fun/(len(age))

print(covariance)

error = np.sqrt(np.diag(covariance))
print(error)

ages_rep = np.arange(0, max(age))
plt.plot(ages_rep, p(ages_rep, result.x[0], result.x[1]))

plt.ylabel("Answer")
plt.xlabel("Age (Years)")

plt.title("Probability fit to Data")

plt.savefig("Data_fit.png")
plt.show()






