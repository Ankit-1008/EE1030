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
x = np.linspace(a, b, 1000)
y_parabola = parabola(x)
y_line = line(x)

# Plotting the area between curves
plt.fill_between(x, y_parabola, y_line, where=(y_line > y_parabola), color='lightblue', label='Area between curves')
plt.plot(x, y_parabola, label=r'$y = x^2$', color='red')
plt.plot(x, y_line, label=r'$y = x$', color='green')
plt.xlabel('x')
plt.ylabel('y')
plt.title(f'Region Between Curves $y = x^2$ and $y = x$\nArea from C: {area_from_c:.5f} square units')
plt.legend()
plt.grid(True)
plt.show()

