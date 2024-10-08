#include <stdio.h>
#include <math.h>

#define N 100000

double parabola(double x) {
    return x * x;
}

double line(double x) {
    return x;
}

double calculate_area(double a, double b) {
    double h = (b - a) / N;
    double area = 0.0;

    for (int i = 0; i < N; i++) {
        double x1 = a + i * h;
        double x2 = a + (i + 1) * h;
        double y1 = line(x1) - parabola(x1);
        double y2 = line(x2) - parabola(x2);
        area += 0.5 * (y1 + y2) * h;
    }

    return area;
}

int main() {
    double a = 0.0, b = 1.0;
    double area = calculate_area(a, b);
    printf("%f\n", area);  // Output the area to stdout
    return 0;
}

