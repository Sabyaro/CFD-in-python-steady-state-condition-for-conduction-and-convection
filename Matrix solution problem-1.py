#Matrix solution

import numpy as np
import matplotlib.pyplot as plt

A = np.array([
    [300,-100,0,0,0],
    [-100,200,-100,0,0],
    [0,-100,200,-100,0],
    [0,0,-100,200,-100],
    [0,0,0,-100,300]
])

T = np.array([
    [200*100],
    [0],
    [0],
    [0],
    [200*500]
])

inv_A = np.linalg.inv(A)

B = inv_A.dot(T)

print(B)

x = np.linspace(0,0.5,5)

plt.plot(x,B)
plt.xlabel('Distance')
plt.ylabel('Temperature')
plt.title('Distance vs temperature for 1D')
plt.grid('True')
plt.show()

