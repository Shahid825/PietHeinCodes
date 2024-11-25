# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 16:17:35 2024

@author: Shahid
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Parameters for the Piet Hein cross-section and the wake
a = 1  # Scale for the Piet Hein cross-section
wake_length = 20  # Length of the wake in the z-direction
wake_amplitude = 0.3  # Amplitude of the wake effect
num_points = 100  # Number of points in each dimension for the meshgrid

# Theta and z ranges for creating the meshgrid
theta = np.linspace(0, 2 * np.pi, num_points)
z = np.linspace(0, wake_length, num_points)
Theta, Z = np.meshgrid(theta, z)

# Modulate the cross-section size to simulate the wake effect
# Incorporating decay and oscillation to simulate a disturbance in a plasmasphere
wake_decay = np.exp(-Z / (wake_length / 2))  # Exponential decay along the wake
wake_oscillation = wake_amplitude * np.sin(2 * np.pi * Z / (wake_length / 4))  # Oscillation along the wake
r = (a + wake_oscillation) * wake_decay  # Combined radius for the wake effect

# Calculating the X and Y coordinates for the wake with the Piet Hein cross-section
X = r * (np.abs(np.cos(Theta)) ** (1/4)) * np.cos(Theta)
Y = r * (np.abs(np.sin(Theta)) ** (1/4)) * np.sin(Theta)

# Plotting the wake with the Piet Hein cross-section
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(Y, Z, X, color='magenta', alpha=0.7)
ax.set_title('Wake with Piet Hein Cross-Section Produced by a Space Object in Plasmasphere')
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')
plt.tight_layout()
plt.show()