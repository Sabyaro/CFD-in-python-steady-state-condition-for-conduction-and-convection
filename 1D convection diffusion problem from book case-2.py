import numpy as np
import matplotlib.pyplot as plt

F = 2.5
D = 0.5

x = 1
N = 5
del_x = np.float64(1/5)

phi_p = np.zeros(N, dtype=np.float64)
phi_p[0] = 1
phi_p[-1] = 0

error = np.float64(1)
tolerance = 1e-8
iteration = 0
max_iterations = 1000  # Set a maximum number of iterations

while error > tolerance and iteration < max_iterations:
    phi = np.copy(phi_p)
    for i in range(N):
        a_E = D + (F / 2)
        a_W = D - (F / 2)
        S_U = 0
        S_P = 0
        a_P = a_E + a_W - S_P
        if i == 0:
            a_E = D - (F / 2)
            a_W = 0
            S_U = D + (F / 2)
            S_P = -3
            a_P = a_E + a_W - S_P
        elif i == N - 1:
            a_E = 0
            a_W = D + (F / 2)
            S_U = 0
            S_P = -2
            a_P = a_E + a_W - S_P
        if i == 0:
            phi[i] = (a_E * phi[i + 1] + S_U) / a_P
        elif i == N - 1:
            phi[i] = (a_W * phi[i - 1] + S_U) / a_P
        else:
            phi[i] = (a_E * phi[i + 1] + a_W * phi[i - 1] + S_U) / a_P
        if np.isnan(phi[i]):
            phi[i] = 0  # Handle NaN values
    error = np.sum(np.abs(phi - phi_p))
    iteration += 1
    print(f"Iteration: {iteration}, Error: {error}")
    phi_p = phi

if iteration == max_iterations:
    print("Maximum iterations reached without convergence.")

xl = np.linspace(0, 1, 5)
phi_x = (2.7183 - np.exp(xl)) / 1.7183

plt.plot(xl, phi, 'o-', label='Numerical Solution')
plt.plot(xl, phi_x, 'x-', label='Analytical Solution')
plt.xlabel('Distance')
plt.ylabel('Convective diffusion')
plt.legend()
plt.grid(True)
plt.show()
