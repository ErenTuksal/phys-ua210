import numpy as np
import matplotlib.pyplot as plt
import scipy

#making a function of the integrand
def integrnd(x,a):
    
    ans = x**(a-1)*np.exp(-x)
    
    return ans

# generating values of x and a
x = np.linspace(0,5)

a = [2,3,4]

# plotting the integrand for different a
for i in a:

    plt.plot(x,integrnd(x,i))





plt.title("Integrand of Gamma Function")
plt.xlabel("x")
plt.ylabel("Integrand")
plt.legend(["a = 2","a = 3","a = 4"])
plt.show()


#defining the new integrand with limits transformed to 0 and 1
def new_integrand(x, a):
    c = a -1
    
    if x < 1:
      
        return (c/(x- 1)**2)*np.exp((a-1)*np.log(c*x/(1-x))-(c*x/(1-x)))
    else:
        return 0

def gamma(a):
# preforming gaussian quadrature 
    
    ans = scipy.integrate.quad(new_integrand, 0, 1,(a))
    return ans[0]

print(gamma(1.5))

#difference of gamma(a) and (a-1)!
dif_1 = gamma(3)- np.math.factorial(2)
print(dif_1)


dif_2 = gamma(6)- np.math.factorial(5)
print(dif_2)


dif_3 = gamma(10)- np.math.factorial(9)
print(dif_3)

plt.savefig("Problem 1 integrand of gamma")