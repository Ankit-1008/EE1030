#include <stdio.h>

#define NUM_POINTS 1000 // Number of points to generate

// Function to generate points for y = x and y = x^2
void generate_points() {
    double x, y1, y2;
    double step_size = 1.0 / NUM_POINTS;

    printf("x\ty = x^2\ty = x\n");
    for (x = 0; x <= 1; x += step_size) {
        y1 = x * x; // y = x^2
        y2 = x;     // y = x
        printf("%lf\t%lf\t%lf\n", x, y1, y2);
    }
}

int main() {
    // Generate points for y = x^2 and y = x
    generate_points();

    return 0;
}

