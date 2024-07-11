# 2D heat conduction problem 

import numpy as np
import matplotlib.pyplot as plt

n = 50

L = 1

T = np.zeros((n,n))
T[0,:] = 1
T[-1,:] = 1

T_new = np.zeros((n,n))
T_new[0,:] = 1
T_new[-1,:] = 1

h = np.float32(L/(n-1))
k = 0.1 #thermal conductivity
A = 0.001 #cross sectional area
iteration = 0
error = 1
tolerance = 1*np.exp(-8)

while error>tolerance:
    for i in range (1,n-1):
        for j in range (1,n-1):

            a_e = np.float32(k*A/h)
            a_w = np.float32(k*A/h)
            a_s = np.float32(k*A/h)
            a_n = np.float32(k*A/h)

            a_p = a_e + a_w +a_s + a_n

            T_new[i,j] = (a_e*T[i,j+1] + a_w*T[i,j-1] + a_s*T[i+1,j] + a_n*T[i-1,j])/(a_p)
    iteration = iteration+1
    print(iteration)     
    error = 0
    for i in range (1, n-1):
        for j in range (1, n-1):
            error = error + np.abs(T[i,j]-T_new[i,j])
    T = T_new.copy()

x_dim = np.arange(n)*h
y_dim = L-np.arange(n)*h
[X,Y] = np.meshgrid(x_dim, y_dim)

plt.contourf(X,Y,T,12)
plt.title('2D heat conduction temperature distribution')
plt.grid('True')
plt.show()