#1D convection problem

#Governing Equation
#T(x0) = 1/4[(Uh+2)T(x0+h)+(2-Uh)T(x0-h)]

import numpy as np
import matplotlib.pyplot as plt
X=1
n = 8 #number of grids
x = np.linspace(0, X, n)

T_old = np.zeros(n)
T_old[0] = 0
T_old[-1] = 1

U = 4 #m/s velocity of fluid
tolerance = 1*np.exp(-4)
error = 1
while error>tolerance:
    T = np.copy(T_old)
    for i in range(n-1):
        T[i] = (1/4)*((0.125*U+2)*T[i+1]+(2-0.125*U)*T[i-1])
    error = np.max(np.abs(T_old-T))
    print(error)
    T_old = T
plt.plot(x,T)
plt.xlabel('distance')
plt.ylabel('temperature')
plt.title('1D convection heat transfer')
plt.grid('True')
plt.show()