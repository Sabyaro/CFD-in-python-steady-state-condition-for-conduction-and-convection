import numpy as np
import matplotlib.pyplot as plt 

L = 0.02
N = 5
del_x = np.float32(0.02/4)

A = 1
k = 0.5 
q = 1000

T_p = np.zeros(N)
T_p[0] = 100
T_p[-1] = 200

iteration = 0
error = 1
tolerance = 1*np.exp(-8)

while error>tolerance: 
    T = np.copy(T_p)
    for i in range (1, N-1):
        a_E = (k*A)/del_x
        a_W = (k*A)/del_x
        S_u = q*A*del_x
        S_p = 0
        a_P = a_E + a_W -S_p
        if i == 1:
            a_E = (k*A)/del_x
            a_W = 0
            S_u = ((2*k*A)/del_x)*100+(q*A*del_x)
            S_p = -((2*k*A)/del_x)
            a_P = a_E - S_p
        if i == N-1:
            a_W = (k*A)/del_x
            a_E = 0
            S_u = ((2*k*A)/del_x)*200+(q*A*del_x)
            S_p = -((2*k*A)/del_x)
            a_P = a_W - S_p
        T[i] = (a_E*T[i+1]+a_W*T[i-1]+S_u)/a_P
        print ('Temperature: ', T[i])
    error = 0
    for i in range (1, N-1):
        error = error + np.abs(T[i]-T_p[i])
    iteration = iteration + 1
    print(iteration)
    T_p = T

x = np.linspace(0,L,N)

plt.plot(x,T)
plt.xlabel('distance')
plt.ylabel('Temperature')
plt.title('1D diffusion problem for constant source')
plt.grid('True')
plt.show()
