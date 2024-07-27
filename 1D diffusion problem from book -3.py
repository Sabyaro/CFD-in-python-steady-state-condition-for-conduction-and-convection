import numpy as np
import matplotlib.pyplot as plt

L = 1
N = 5
del_x = np.float32(L/N)

T_p = np.zeros(N)
T_p[0] = 100
T_p[-1] = 20

error = 1
tolerance = 1*np.exp(-8)
iteration = 0

n = 5
while error>tolerance:
    T = np.copy(T_p)
    for i in range (0, N-1):
        a_E = 1/del_x 
        a_W = 1/del_x
        S_u = n**2*del_x*20
        S_p = -n**2*del_x
        a_p = a_E + a_W -S_p
        if i == 0: 
            a_E = 1/del_x
            a_W = 0
            S_u = (n**2*del_x*20) + (2/del_x)*100
            S_p = -((2/del_x)+(n**2*del_x))
            a_p = a_E -S_p
        if i==N-1:
            a_E = 0
            a_W = 1/del_x 
            S_u = n**2*del_x*20
            S_p = -n**2*del_x
            a_p = a_W -S_p
        T[i] = (a_E*T[i+1]+a_W*T[i-1]+S_u)/a_p 

    error = 0
    for i in range (0, N-1):
        error = error + np.abs(T[i]-T_p[i])
    iteration = iteration+1
    print(iteration)
    T_p = T

x = np.linspace(0,1,N)
plt.plot(x,T)
plt.xlabel('Distance')
plt.ylabel('Temperature')
plt.title('1D diffusion problem')
plt.grid('True')
plt.show()