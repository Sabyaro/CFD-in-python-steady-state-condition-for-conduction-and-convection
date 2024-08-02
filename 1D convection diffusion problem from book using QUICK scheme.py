import numpy as np
import matplotlib.pyplot as plt

x = 1
N = 5
del_x = np.float64(x/N)

phi_p = np.zeros(N)
phi_p[0]=1
phi_p[-1]=0

error = 1
tolerance = 1*np.exp(-8)
iteration = 0

F = 0.2
D = 0.5

max_iteration = 10000

while error>tolerance and iteration<max_iteration:
    phi_Q = np.copy(phi_p)
    phi_N = np.copy(phi_p)
    for i in range(0,N-1):
        a_E_Q = D-((3/8)*F)
        a_W_Q = (D+F)
        S_U_Q = -(F*phi_Q[0])/4
        S_P_Q = (F)/4
        a_WW_Q = 0
        a_P_Q = a_E_Q+a_W_Q+a_WW_Q-S_P_Q
        a_E_N = D
        a_W_N = D+F
        S_U_N = 0 
        S_P_N = 0
        a_P_N = a_E_N + a_W_N - S_P_N
        if i==0:
            a_WW_Q = 0
            a_W_Q = 0
            a_E_Q = (2.33*D)-(3/8)*F
            S_U_Q = ((16/3)*D+(1.67)*F)*phi_Q[0]
            S_P_Q = -((16/3)*D+(1.67)*F)
            a_P_Q = a_E_Q+a_W_Q+a_WW_Q-S_P_Q
            a_E_N = D
            a_W_N = 0
            S_U_N = (2*D+F)
            S_P_N = -(2*D+F)
            a_P_N = a_E_N + a_W_N -S_P_N 
        if i==N-1:
            a_WW_Q = -(1/8)*F
            a_E_Q = 0
            a_W_Q = (2+(1/3))*D+(6/8)*F
            S_U_Q = ((16/3)*D-F)*phi_Q[-1]
            S_P_Q = -((16/3)*D-F)
            a_P_Q = a_E_Q+a_W_Q+a_WW_Q-S_P_Q
            a_E_N = 0
            a_W_N = D+F
            S_U_N = 0
            S_P_N = -2*D
            a_P_N = a_E_N + a_W_N -S_P_N
        phi_N[i] = (a_E_N*phi_N[i+1]+a_W_N*phi_N[i-1]+S_U_N)/a_P_N
        phi_Q[i] = (a_E_Q*phi_Q[i+1]+a_W_Q*phi_Q[i-1]+S_U_Q+a_WW_Q*phi_Q[i-2])/a_P_Q 
    
    error = 0
    for i in range(0,N-1):
        error = error + np.abs(phi_p[i]-phi_Q[i])
    iteration = iteration+1
    print(iteration)
    phi_Q = phi_p

xl = np.linspace(0,1,5)
phi_x = 1+((1-np.exp(25*xl))/(7.20*10**6))

plt.plot(xl,phi_N)
plt.plot(xl,phi_Q)
plt.plot(xl,phi_x)
plt.xlabel('distance')
plt.ylabel('Convection diffusion')
plt.grid('True')
plt.legend(['Upwind scheme', 'QUICK scheme', 'Exact solution'])
plt.show()
