#Matrix solution of problem-2 

import numpy as np
import matplotlib.pyplot as plt

A = np.array([
    [375,-125,0,0,0],
    [-125,250,-125,0,0],
    [0,-125,250,-125,0],
    [0,0,-125,250,-125],
    [0,0,0,-125,375]
])

T = np.array([
    [4000+250*100],
    [4000],
    [4000],
    [4000],
    [4000+250*200]
])

inv_A = np.linalg.inv(A)

B = inv_A.dot(T)

print(B)

x = np.linspace(0,2,5)

plt.plot(x,B)
plt.xlabel('Distance')
plt.ylabel('Temperature')
plt.title('Distance vs Temperature 1D diffusion problem')
plt.grid('True')
plt.show()