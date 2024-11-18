#include <stdio.h>
#include <math.h>
#include <stdlib.h>

#define MAX_ITER 1000
#define TOL 1e-6

// Function prototypes
void qr_decomposition(int n, double A[n][n], double Q[n][n], double R[n][n]);
void multiply_matrices(int n, double A[n][n], double B[n][n], double C[n][n]);
void print_matrix(int n, double matrix[n][n]);
int is_diagonal(int n, double matrix[n][n]);

// QR algorithm to compute eigenvalues
void qr_algorithm(int n, double A[n][n], double eigenvalues[n]) {
    double Q[n][n], R[n][n];
    double Ak[n][n];
    
    // Copy A into Ak for iterative computation
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            Ak[i][j] = A[i][j];
        }
    }

    for (int iter = 0; iter < MAX_ITER; iter++) {
        // Perform QR decomposition on Ak
        qr_decomposition(n, Ak, Q, R);
        
        // Recompose Ak = R * Q
        multiply_matrices(n, R, Q, Ak);
        
        // Check if Ak is close to diagonal
        if (is_diagonal(n, Ak)) {
            break;
        }
    }

    // Extract eigenvalues from diagonal of Ak
    for (int i = 0; i < n; i++) {
        eigenvalues[i] = Ak[i][i];
    }
}

// QR decomposition using Modified Gram-Schmidt
void qr_decomposition(int n, double A[n][n], double Q[n][n], double R[n][n]) {
    // Initialize Q and R
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            Q[i][j] = 0.0;
            R[i][j] = 0.0;
        }
    }

    // Gram-Schmidt process
    for (int j = 0; j < n; j++) {
        // Copy column j of A into column j of Q
        for (int i = 0; i < n; i++) {
            Q[i][j] = A[i][j];
        }

        // Orthogonalize against previous columns
        for (int k = 0; k < j; k++) {
            double dot = 0.0;
            for (int i = 0; i < n; i++) {
                dot += Q[i][k] * Q[i][j];
            }
            R[k][j] = dot;
            for (int i = 0; i < n; i++) {
                Q[i][j] -= R[k][j] * Q[i][k];
            }
        }

        // Compute the norm of Q[j]
        double norm = 0.0;
        for (int i = 0; i < n; i++) {
            norm += Q[i][j] * Q[i][j];
        }
        norm = sqrt(norm);

        // Avoid division by zero
        if (fabs(norm) < TOL) {
            norm = TOL;
        }
        R[j][j] = norm;

        // Normalize column j of Q
        for (int i = 0; i < n; i++) {
            Q[i][j] /= R[j][j];
        }
    }
}

// Function to multiply two matrices A and B into C
void multiply_matrices(int n, double A[n][n], double B[n][n], double C[n][n]) {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            C[i][j] = 0.0;
            for (int k = 0; k < n; k++) {
                C[i][j] += A[i][k] * B[k][j];
            }
        }
    }
}

// Check if a matrix is close to diagonal
int is_diagonal(int n, double matrix[n][n]) {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (i != j && fabs(matrix[i][j]) > TOL) {
                return 0;
            }
        }
    }
    return 1;
}

// Function to print a matrix
void print_matrix(int n, double matrix[n][n]) {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            printf("%8.4f ", matrix[i][j]);
        }
        printf("\n");
    }
    printf("\n");
}

// Main function
int main() {
    int n = 3;
    double A[3][3] = {
        {2, 0, 0},
        {0, 2, 0},
        {0, 0, 2}
    };
    double eigenvalues[3];

    printf("Original matrix A:\n");
    print_matrix(n, A);

    // Perform QR algorithm
    qr_algorithm(n, A, eigenvalues);

    // Print eigenvalues
    printf("Eigenvalues:\n");
    for (int i = 0; i < n; i++) {
        printf("%8.4f\n", eigenvalues[i]);
    }

    return 0;
}


