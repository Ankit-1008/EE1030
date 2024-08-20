import matplotlib.pyplot as plt

# Define your x and y values
x = [-1, 0.8, 2]
y = [3, 4.2, 5]
# Create a plot
plt.plot(x, y, marker='o')  # 'marker' adds points at each coordinate

# Add labels to the axes
plt.xlabel('X axis')
plt.ylabel('Y axis')

# Add a title
plt.title('Line plot connecting X and Y points')

# Annotate the points with their coordinates
for i in range(len(x)):
    plt.annotate(f'({x[i]}, {y[i]})', (x[i], y[i]), textcoords="offset points", xytext=(5,5), ha='center')

# Display the plot
plt.show()

