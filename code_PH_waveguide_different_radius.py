# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 13:12:52 2024

@author: Shahid
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the number of points in the meshgrid for theta and z
num_points = 100
theta = np.linspace(0, 2 * np.pi, num_points)
z = np.linspace(-10, 10, num_points)

# Create the meshgrid for theta and z
Theta, Z = np.meshgrid(theta, z)

# Define the super-ellipse function
def super_ellipse(theta, a=1, rho=1):
    # Returns the x and y coordinates based on the super-ellipse equation
    # x^4 + y^4 = rho^4
    x = rho * np.sign(np.cos(theta)) * (np.abs(np.cos(theta)))**(1/4)
    y = rho * np.sign(np.sin(theta)) * (np.abs(np.sin(theta)))**(1/4)
    return x, y

# Generate the Piet Hein waveguide
a = 1  # Scale parameter for the super-ellipse
rho_values = [0.8, 1, 1.2]  # Different rho values to show the waveguide's shape
colors = ['r', 'g', 'b']  # Colors for the different rho values
labels = [f'ρ = {rho}' for rho in rho_values]  # Labels for the legend

# Plotting the Piet Hein waveguide
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot the super-ellipse for different rho values to illustrate the waveguide's shape
for rho, color, label in zip(rho_values, colors, labels):
    X, Y = super_ellipse(Theta, a, rho)
    ax.plot_surface(X, Z, Y, rstride=5, cstride=5, color=color, alpha=0.5, label=label)

# Create a legend for the different rho values
ax.legend(loc='upper right')

ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')
ax.set_title('3D Visualization of the Piet Hein Waveguide with different \rho values')

# Avoid cutting off the legend
plt.tight_layout()

plt.show()