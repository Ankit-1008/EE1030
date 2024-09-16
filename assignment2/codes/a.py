import matplotlib.pyplot as plt

# Function to find points dividing a line segment into n equal parts
def divide_line(A, B, n):
    points = []
    for i in range(1, n):
        x = (i * B[0] + (n - i) * A[0]) / n
        y = (i * B[1] + (n - i) * A[1]) / n
        points.append((x, y))
    return points

# Points A and B
A = (-2, 2)
B = (2, 8)

# Divide the line into 4 equal parts
dividing_points = divide_line(A, B, 4)

# Add points A and B to the list for plotting
points = [A] + dividing_points + [B]

# Create a figure and axis
fig, ax = plt.subplots()

# Extract x and y values
x_values = [point[0] for point in points]
y_values = [point[1] for point in points]

# Plot the line segment and points
ax.plot(x_values, y_values, marker='o', color='blue', linestyle='-', markersize=8)

# Add labels to the points
ax.text(A[0], A[1], 'A(-2, 2)', fontsize=12, ha='right', va='bottom')
for i, point in enumerate(dividing_points, start=1):
    ax.text(point[0], point[1], f'R{i}{point}', fontsize=12, ha='right', va='bottom')
ax.text(B[0], B[1], 'B(2, 8)', fontsize=12, ha='right', va='bottom')

# Set limits and grid
ax.set_xlim(-3, 3)
ax.set_ylim(0, 10)
ax.grid(True)

# Set labels for axes
ax.set_xlabel('$x$')
ax.set_ylabel('$y$')

# Set title
plt.title('Division of Line Segment into Four Equal Parts')

# Show the plot
plt.grid()
plt.savefig("Figure_1.png")
plt.show()

