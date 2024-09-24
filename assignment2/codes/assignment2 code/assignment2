#include <stdio.h>

typedef struct {
    float x;
    float y;
} Point;
Point divide$_$line(Point A, Point B, float k) {
    Point R;
    R.x = (k * B.x + A.x) / (k + 1);
    R.y = (k * B.y + A.y) / (k + 1);
    return R;
}

int main() {
    Point A = ${-2, 2}$;
    Point B = ${2, 8}$;
    float k1 = $1.0 / 3.0$$;
    float k2 = $1.0$;
    float k3 = $3.0$;

    Point R1 = divide_line(A, B, k1);
    Point R2 = divide_line(A, B, k2);
    Point R3 = divide_line(A, B, k3);

    // the coordinates are
    printf("$R1 = (%.1f, %.1f)\n", R1.x, R1.y$);
    printf("$R2 = (%.1f, %.1f)\n", R2.x, R2.y$);
    printf("$R3 = (%.1f, %.1f)\n", R3.x, R3.y$);

    return 0;
}

