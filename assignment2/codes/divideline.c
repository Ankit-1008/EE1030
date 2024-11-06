#include <stdio.h>

// Define a structure for a point
typedef struct {
    float x;
    float y;
} Point;

// Function to divide the line segment into n equal parts
void divide_line(Point A, Point B, int n, FILE *file) {
    fprintf(file, "Dividing into %d parts:\n", n);
    for (int i = 1; i < n; i++) {
        float x = (i * B.x + (n - i) * A.x) / n;
        float y = (i * B.y + (n - i) * A.y) / n;
        fprintf(file, "%.2f %.2f\n", x, y);  // Write the point to the file
    }
    fprintf(file, "\n");
}

int main() {
    // Define points A and B
    Point A = {-2, 2};
    Point B = {2, 8};

    // Open a file to store the output points
    FILE *file = fopen("points.txt", "w");

    if (file == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    // Divide the line for different values of k and write the results to the file
    divide_line(A, B, 3, file);  // Divide into 3 parts
    divide_line(A, B, 4, file);  // Divide into 4 parts
    divide_line(A, B, 5, file);  // Divide into 5 parts

    // Close the file
    fclose(file);

    printf("Points computed and written to 'points.txt'.\n");
    return 0;
}

