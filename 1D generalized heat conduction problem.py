# 1D generalized heat conduction problem 
import numpy as np
import matplotlib.pyplot as plt

X =1 
n = 8 #number of grids 
x = np.linspace(0,X,n)

k = 0.01 #thermal conductivity
A = 0.002 #cross sectional area 

T_old = np.zeros(n)
T_old[0] = 0
T_old[-1] = 1
error = 1
tolerance = 1*np.exp(-4)

while error>tolerance:
    T = np.copy(T_old)
    for i in range (0, n-1):
        a_e = (k*A)/0.125
        a_w = (k*A)/0.125
        a_p = a_e+a_w
        if i==0:
            a_w = 0
            a_p = a_e
        T[i] = (a_e*T[i+1]+a_w*T[i-1])/a_p
    error = np.max(np.abs(T_old-T))
    T_old = T

plt.plot(x,T)
plt.xlabel('distance')
plt.ylabel('temperature')
plt.title('1D generalized heat conduction problem')
plt.grid('True')
plt.show()
        