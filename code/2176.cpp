#include <stdio.h>
#include <stdlib.h>

#define N  31
int x[N][N][N] = {0};

int f(int a, int b, int c) {
    if (a <= 0 || b <= 0 || c <= 0)
        return 1;
    if (a > 20 || b > 20 || c > 20)
        return f(20, 20, 20);
    if (x[a][b][c] != 0)
        return x[a][b][c];
    if (a < b && b < c)
        return x[a][b][c] =
                       f(a, b, c - 1) +
                       f(a, b - 1, c - 1) -
                       f(a, b - 1, c - 1);
    return x[a][b][c] =
                   f(a - 1, b, c) +
                   f(a - 1, b - 1, c) +
                   f(a - 1, b, c - 1) -
                   f(a - 1, b - 1, c - 1);
}

int main() {
    int a, b, c;
    while (scanf("%d %d %d", &a, &b, &c) != EOF) {
        printf("%d\n", f(a, b, c));
    }
    return 0;
}