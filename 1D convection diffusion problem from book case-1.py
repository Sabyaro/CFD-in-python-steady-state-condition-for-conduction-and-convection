import numpy as np
import matplotlib.pyplot as plt 

F = 0.1 
D = 0.5

x = 1
N = 5
del_x = np.float32(1/5)

phi_p = np.zeros(N)
phi_p[0] = 1
phi_p[-1] = 0

error = 1
tolerance = 1*np.exp(-8)
iteration = 0

while error>tolerance:
    phi = np.copy(phi_p)
    for i in range (0,N-1):
        a_E = D+(F/2)
        a_W = D-(F/2)
        S_U = 0
        S_P = 0
        a_P = a_E + a_W -S_P
        if i==0:
            a_E = D-(F/2)
            a_W = 0
            S_U = (D+(F/2))
            S_P = -(D+F)
            a_P = a_E + a_W - S_P
        if i==N-1:
            a_E = 0
            a_W = D+(F/2)
            S_U = 0
            S_P = -(D-F)
            a_P = a_E + a_W -S_P 
        phi[i] = (a_E*phi[i+1]+a_W*phi[i-1]+S_U)/a_P 
    error = 0
    for i in range (0,N-1):
        error = error + np.abs(phi[i]-phi_p[i])
    iteration = iteration +1
    print(iteration)
    phi_p = phi

xl = np.linspace(0,1,5)
plt.plot(xl,phi)
plt.xlabel('Distance')
plt.ylabel('Convection diffusion')
plt.grid('True')
plt.title('1D convection diffusion problem')
plt.show()
