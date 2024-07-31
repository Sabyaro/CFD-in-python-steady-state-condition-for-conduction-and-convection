import numpy as np
import matplotlib.pyplot as plt

x = 1
N = 5
del_x = np.float64(x/N)

phi_p = np.zeros(N)
phi_p[0] = 1
phi_p[-1] = 0

D = 0.5
F = 2.5

error =1 
tolerance = 1*np.exp(-8)
iteration = 0 

while error>tolerance:
    phi = np.copy(phi_p)
    for i in range (0,N-1):
        a_E = D
        a_W = D+F
        S_U = 0 
        S_P = 0
        a_P = a_E + a_W - S_P
        if i==0: 
            a_E = D
            a_W = 0
            S_U = (2*D+F)
            S_P = -(2*D+F)
            a_P = a_E + a_W -S_P
        if i==N-1: 
            a_E = 0
            a_W = D+F
            S_U = 0
            S_P = -2*D
            a_P = a_E + a_W -S_P 
        phi[i] = (a_E*phi[i+1]+a_W*phi[i-1]+S_U)/a_P

    error = 0
    for i in range(0,N-1):
        error = error + np.abs(phi[i]-phi_p[i])
    iteration +=1
    print(iteration)
    phi_p = phi

xl = np.linspace(0,1,5)
phi_x = ((2.7183-np.exp(xl))/1.7183)
plt.plot(xl,phi)
plt.plot(xl,phi_x)
plt.xlabel('Distance')
plt.ylabel('Convective diffusion')
plt.grid('True')
plt.legend(['Numerical Solution', 'Analytical Solution'])
plt.show()
