# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 14:55:58 2024

@author: Shahid
"""

import numpy as np
import matplotlib.pyplot as plt

# Set the parameter for the Piet Hein curve
a = 1  # You can change this value based on your requirements

# Define a range of x values from -a to a
x_values = np.linspace(-a, a, 50)

# Calculate y values for the Piet Hein curve: x^4 + y^4 = a^4
y_values_ph = (a**4 - x_values**4)**0.25
y_values_ph = np.nan_to_num(y_values_ph)  # Convert NaNs to 0 for plotting

# Calculate y values for the perpendicular curve: 1/x^2 - 1/y^2 = 1/a^2
# This requires a bit more work since it involves a reciprocal relation
# We'll plot this curve for several values of ξ by defining a function

def y_values_perp(x, xi):
    # Avoid division by zero
    x_nonzero = np.where(x != 0, x, np.nan)
    return np.sqrt(1 / (1/x_nonzero**2 - 1/xi**2))

# Set values of ξ for which the perpendicular curves are to be plotted
xi_values = [0.5, 1, 1.5, 2]

# Create the plot
plt.figure(figsize=(8, 8))

# Plot the Piet Hein curve
plt.plot(x_values, y_values_ph, 'b', label='Piet Hein curve ($x^4 + y^4 = a^4$)')
plt.plot(x_values, -y_values_ph, 'b')  # The other half

# Plot the perpendicular curves
for xi in xi_values:
    y_perp = y_values_perp(x_values, xi)
    plt.plot(x_values, y_perp, '--', label=f'Perp. curve at ξ={xi}')
    plt.plot(x_values, -y_perp, '--')  # The other half

# Formatting the plot
plt.title('Piet Hein and Perpendicular Curves')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True)
plt.legend()
plt.axis('equal')  # Ensure x and y have the same scale

# Show the plot
plt.show()