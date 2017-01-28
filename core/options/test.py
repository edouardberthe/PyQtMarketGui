from math import *

import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

# Dynamics

S0 = 100
r = 0.05
sigma = 0.3

# Contract
T = 1
K = 80

# Finite Difference
SMin = 0; SMax = 100
M = 100
N = 1000

# Grid
S = np.linspace(SMin, SMax, M+1)
dS = (SMax - SMin) / M
dt = T / N

V = np.zeros((M+1, N+1))

V[:, N] = np.maximum(K - S, 0)

p_wing = sigma**2 * S[1:-1]**2 * dt / dS**2
p_asym = r * S[1:-1] * dt / (2 * dS)

p_up = p_wing / 2 + p_asym
p_middle = 1 - p_wing
p_down = p_wing / 2 - p_asym
print(p_up, p_middle, p_down)

for j in range(N-1, -1, -1):
    V[1:-1, j] = 1 / (1 + r*dt) * (
        p_up * V[2:, j+1]
        + p_middle * V[1:-1, j+1]
        + p_down * V[:-2, j+1])
    V[0, j] = K * exp(- r * (N - j) * dt)
    V[-1, j] = 0

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

X, Y = np.meshgrid(np.linspace(0, T, N+1), S)
ax.plot_surface(X, Y, V)
plt.show()
