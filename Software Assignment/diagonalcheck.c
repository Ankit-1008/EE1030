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
