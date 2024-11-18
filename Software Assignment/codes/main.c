int main() {
    int n;
    printf("Enter the size of the matrix (n x n): ");
    scanf("%d", &n);

    double A[n][n];
    double eigenvalues[n];

    printf("Enter the elements of the %d x %d matrix row by row:\n", n, n);
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            printf("A[%d][%d]: ", i + 1, j + 1);
            scanf("%lf", &A[i][j]);
        }
    }

    printf("\nOriginal matrix A:\n");
    print_matrix(n, A);

    qr_algorithm(n, A, eigenvalues);

    printf("Eigenvalues:\n");
    for (int i = 0; i < n; i++) {
        printf("%8.4f\n", eigenvalues[i]);
    }

    return 0;
}
