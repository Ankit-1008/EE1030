import numpy as np
import matplotlib.pyplot as plt

# Define x values from -3 to 3
x = np.linspace(-3, 3, 500)

# Define the parabola y = x^2
y_lower = x**2

# Create the figure and axes
fig, ax = plt.subplots()

# Plot the parabola y = x^2
ax.plot(x, y_lower, label=r'$y = x^2$', color='blue')

# Adding the line segment from A(2, 1) to B(-1, 0.25)
x_line = np.array([-1, 2])
y_line = np.array([0.25, 1])
ax.plot(x_line, y_line, color='orange', label="line")

# Mark points A(2, 1) and B(-1, 0.25)
ax.scatter([2, -1], [1, 0.25], color='black')
ax.text(2, 1, 'A(2, 1)', fontsize=10, ha='left', va='top')
ax.text(-1, 0.25, 'B(-1, 0.25)', fontsize=10, ha='left', va='top')

# Set axis limits and labels
ax.set_xlim(-3, 3)
ax.set_ylim(-1, 3)
ax.set_xlabel('x')
ax.set_ylabel('y')

# Adding gridlines and equal aspect ratio
ax.grid(True)
ax.set_aspect('equal')

# Save the figure as a PNG file
plt.savefig('fig.png')  

# Show the plot
plt.show()

