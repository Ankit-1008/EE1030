void qr_algorithm(int n, double A[n][n], double eigenvalues[n]) {
    double Q[n][n], R[n][n];
    double Ak[n][n];
    
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            Ak[i][j] = A[i][j];
        }
    }

    for (int iter = 0; iter < MAX_ITER; iter++) {
        qr_decomposition(n, Ak, Q, R);
        multiply_matrices(n, R, Q, Ak);
        if (is_diagonal(n, Ak)) {
            break;
        }
    }

    for (int i = 0; i < n; i++) {
        eigenvalues[i] = Ak[i][i];
    }
}
