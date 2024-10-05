#include <stdio.h>
#include <math.h>

#define N 100000  // Number of trapezoids (higher value increases precision)

// Function definitions for the curves
double parabola(double x) {
    return x * x;  // y = x^2
}

double line(double x) {
    return x;  // y = x
}

// Function to calculate area using the trapezoidal rule
double calculate_area(double a, double b) {
    double h = (b - a) / N;  // Width of each trapezoid
    double area = 0.0;  // Initialize total area

    for (int i = 0; i < N; i++) {
        double x1 = a + i * h;
        double x2 = a + (i + 1) * h;
        
        // Calculate the height of the trapezoid
        double y1 = line(x1) - parabola(x1);  // Difference between y = x and y = x^2
        double y2 = line(x2) - parabola(x2);

        // Add area of the trapezoid
        area += 0.5 * (y1 + y2) * h;
    }
    return area;
}

int main() {
    double a = 0.0;  // Lower limit of integration (x = 0)
    double b = 1.0;  // Upper limit of integration (x = 1)

    double area = calculate_area(a, b);

    printf("The area of the region between the curves y = x^2 and y = x is: %f square units\n", area);

    return 0;
}

