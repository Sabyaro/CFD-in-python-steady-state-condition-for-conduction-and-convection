import numpy as np
import matplotlib.pyplot as plt

L = 0.5
del_x = 0.1 #grid size

N = np.int32(L/del_x) #Number of grid (mesh number)

#Boundary condition
T_p = np.zeros(N)
T_p[0] = 100
T_p[-1] = 500

x = np.linspace(0,0.5,N)

k = 1000 #Thermal conductivity
A = 10*10**(-3) #The cross sectional area 

#Convergence Criteria
error = 1
tolerance = 1*np.exp(-8)
iteration = 0

while error>tolerance:
    T = np.copy(T_p)
    for i in range(0,N-1):
        a_E = (k*A)/del_x
        a_W = (k*A)/del_x
        S_u = 0
        S_p = 0
        a_p = a_E +a_W-S_p

        if  i==0:
            S_u = 100*((2*k*A)/del_x)
            S_p = -(2*k*A)/del_x
            a_W = 0
            a_p = a_E - S_p 
        if i==N-1:
            S_u = 500*((2*k*A)/del_x)
            S_p = -(2*k*A)/del_x
            a_E = 0
            a_p = a_W-S_p
        T[i] = (a_E*T[i+1]+a_W*T[i-1]+S_u)/a_p #Governing equation
        print('Temperature: ',T[i])
    error = 0
    for i in range(0,N-1):
        error = error+np.abs(T_p[i]-T[i])
    
    iteration = iteration+1
    print(iteration)
    T_p = T

#Data plotting 
plt.plot(x,T)
plt.xlabel('Distance')
plt.ylabel('Temperature')
plt.title('1D diffusion problem')
plt.grid('True')
plt.show()