# Code by GVV Sharma
# July 22, 2024
# Released under GNU GPL
# Line 

import sys                                          # for path to external scripts
sys.path.insert(0, '/ankit/Documents/matgeo/codes/book')  # path to my scripts
import numpy as np
import matplotlib.pyplot as plt


# Define points and direction vectors
a1 = np.array([1, 1, 0])        # Point on line l1
b1 = np.array([2, -1, 1])       # Direction vector of line l1

a2 = np.array([2, 1, -1])       # Point on line l2
b2 = np.array([3, -5, 2])       # Direction vector of line l2

# Step 1: Calculate the vector connecting the two lines
a = a2 - a1

# Step 2: Calculate the cross product of the direction vectors
cross_product = np.cross(b1, b2)

# Step 3: Calculate the magnitude of the cross product
cross_product_magnitude = np.linalg.norm(cross_product)

# Step 4: Calculate the dot product (a2 - a1) · (b1 × b2)
dot_product = np.abs(np.dot(a, cross_product))

# Step 5: Calculate the shortest distance
if cross_product_magnitude != 0:
    distance = dot_product / cross_product_magnitude
else:
    distance = np.inf  # Lines are parallel, distance is undefined

# Print the shortest distance
print(f"The shortest distance between the lines is: {distance:.4f}")

# Plotting the lines for visualization
# Line 1
t1 = np.linspace(-5, 5, 100)
line1 = a1[:, None] + b1[:, None] * t1  # Parametric equation for line l1

# Line 2
t2 = np.linspace(-5, 5, 100)
line2 = a2[:, None] + b2[:, None] * t2  # Parametric equation for line l2

# Create a 3D plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot the lines
ax.plot(line1[0, :], line1[1, :], line1[2, :], label='Line l1', color='b')
ax.plot(line2[0, :], line2[1, :], line2[2, :], label='Line l2', color='r')

# Mark points A and B
ax.scatter(a1[0], a1[1], a1[2], color='blue', s=100, label='Point A (1, 1, 0)')
ax.scatter(a2[0], a2[1], a2[2], color='red', s=100, label='Point B (2, 1, -1)')

# Add labels
ax.text(a1[0], a1[1], a1[2], 'A', color='blue', fontsize=12)
ax.text(a2[0], a2[1], a2[2], 'B', color='red', fontsize=12)

# Set labels for axes
ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
ax.set_zlabel('$z$')
ax.legend()
ax.grid()

plt.show()
