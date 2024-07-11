# 2D heat convection problem with Peclet number 

import numpy as np
import matplotlib.pyplot as plt

L = 1
n = 50 
h = np.float32(L/(n-1))
#diffusivity 
gamma = np.float32(0.1)

#velocity 
u = np.float32(0.5)
v = np.float32(0.3)

#density 
rho = np.float32(1)

T = np.zeros((n,n))
T[0,:] = 100
T[n-1,:] = 500

T_new = np.zeros((n,n))
T_new[0,:] = 100
T_new[n-1,:] = 500

error = 1
tolerance = 1*np.exp(-8)
iteration = 0

while error>tolerance: 
    for i in range (1, n-1):
        for j in range (1, n-1):
            a_e = np.float32((gamma/h)-(rho*u)/2)
            a_w = np.float32((gamma/h)+(rho*u)/2)
            a_n = np.float32((gamma/h)-(rho*v)/2)
            a_s = np.float32((gamma/h)+(rho*v)/2)
            a_p = a_e+a_w+a_n+a_s
            T_new[i,j] = (a_e*T[i,j+1]+a_w*T[i,j-1]+a_n*T[i-1,j]+a_s*T[i+1,j])/a_p
    error = 0
    for i in range(1,n-1):
        for j in range(1,j-1):
            error = error+np.abs(T[i,j]-T_new[i,j])
    iteration = iteration+1
    T=T_new.copy()
    print(iteration)

x_dim = np.arange(n)*h
y_dim = L-np.arange(n)*h
[X,Y] = np.meshgrid(x_dim,y_dim)

plt.contourf(X,Y,T,12)
plt.title("2D heat convection temperature distribution")
plt.grid('True')
plt.show()