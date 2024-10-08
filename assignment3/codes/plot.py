import numpy as np
import matplotlib.pyplot as plt
import subprocess

# Define the functions for the curves
def parabola(x):
    return x ** 2  # y = x^2

def line(x):
    return x  # y = x

# Define the limits of integration
a, b = 0.0, 1.0

# Run the compiled C program and capture the output
result = subprocess.run(["./area_calculator"], capture_output=True, text=True)

# Get the output (area) from the C program
area_from_c = float(result.stdout.strip())

# Print the result from the C program
print(f"Area read from C program: {area_from_c:.5f}")

# Plotting the region between the curves
x_values = np.linspace(-2, 2, 1000)  # Extend the range for both parabola and line
y_parabola = parabola(x_values)
y_line = line(x_values)

# Calculate the intersection points (x=0 and x=1)
intersection_x = [0, 1]
intersection_y = [parabola(0), line(1)]

# Plotting the curves
plt.plot(x_values, y_parabola, label=r'$y = x^2$', color='red')  # Full parabola
plt.plot(x_values, y_line, label=r'$y = x$', color='green')      # Full line

# Add intersection points
plt.scatter(intersection_x, intersection_y, color='blue', zorder=5, label='Intersection points')

# Label the intersection points
for i, (xi, yi) in enumerate(zip(intersection_x, intersection_y)):
    plt.text(xi, yi, f'({xi:.1f}, {yi:.1f})', fontsize=10, verticalalignment='bottom')

plt.xlabel('x')
plt.ylabel('y')
plt.title(f'Region Between Curves $y = x^2$ and $y = x$\nArea from C: {area_from_c:.5f} square units')
plt.legend()
plt.grid(True)

# Adjust axis limits to show the full parabola and line in all quadrants
plt.xlim([-2, 2])  # Show more of the parabola and the line across quadrants
plt.ylim([-2, 4])  # Include more of the lower half (quadrants III and IV)

# Display the plot
plt.show()

