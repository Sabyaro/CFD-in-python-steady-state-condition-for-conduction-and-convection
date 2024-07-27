#Matrix solution of problem-3

import numpy as np
import matplotlib.pyplot as plt

A = np.array([
    [20,-5,0,0,0],
    [-5,15,-5,0,0],
    [0,-5,15,-5,0],
    [0,0,-5,15,-5],
    [0,0,0,-5,10]
])

T = np.array([
    [1100],
    [100],
    [100],
    [100],
    [100]
])

B = np.linalg.inv(A).dot(T)

x = np.linspace(0,0.5,5)

plt.plot(x,B)
plt.xlabel('Distance')
plt.ylabel('Temperature')
plt.title('Distance vs Temperature 1D diffusion problem')
plt.grid('True')
plt.show()