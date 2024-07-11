# 1D convection problem using generalized equation

import numpy as np
import matplotlib.pyplot as plt

L = 1
N = 50
h = np.float32(L/(N-1))

#diffusivity
gamma = np.float32(0.1)

#velocity 
u = np.float32(1)

#density 
rho = np.float32(1.0)

#peclet number 
Pe = (rho*h*u)/gamma


T = np.zeros(N)
T[0] = 100
T[N-1] = 500

T_new = np.zeros(N)
T_new[0] = 100
T_new[N-1] = 500

tolerance = 1*np.exp(-8)
error = 1
iteration = 0

while error>tolerance:
    for i in range (1, N-1):
        a_e = np.float32((gamma/h) + max(-(rho*u),0))
        a_w = np.float32((gamma/h) + max((rho*u,0)))
        a_p = a_e + a_w
        T_new[i] = (a_e*T[i+1] + a_w*T[i-1])/a_p
    
    error = 0
    for i in range (1, N-1):
        error = error + np.abs(T[i]-T_new[i])
    
    iteration = iteration+1
    print(iteration)
    T = T_new.copy()

print("Peclet Number: ",Pe)
x = np.arange(N)*h
plt.plot(x,T)
plt.xlabel('dimension')
plt.ylabel('temperature')
plt.title('1D convection problem')
plt.show()

