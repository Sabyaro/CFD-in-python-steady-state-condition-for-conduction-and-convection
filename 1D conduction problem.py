#1D conduction problem

import numpy as np 
import matplotlib.pyplot as plt 

X =1 
h = 0.125   #grid spacing/meshing

x = np.linspace(0, X, 8)

T_old = np.zeros(8)
tolerance_value = 1*np.exp(-4)
error = 1
T_old[0]=0
T_old[7]=1
while (error>tolerance_value):
    T = np.copy(T_old)
    for i in range(7):
        T[i] = (1/2)*(T[i+1]+T[i-1])
    
    error = np.max(np.abs(T-T_old))
    print(error)
    T_old = T
plt.plot(x, T)
plt.xlabel("distance")
plt.ylabel("temperature")
plt.title("The 1D heat conduction problem")
plt.grid("True")
plt.show()
    

