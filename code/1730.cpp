#include<bits/stdc++.h>

using namespace std;

int main() {
    int s[100][100], a[100][100], n, i, j;
    cin >> n;
    for (i = 0; i < n; i++)
        for (j = 0; j <= i; j++)
            cin >> a[i][j];
    for (j = 0; j < n; j++)
        s[n - 1][j] = a[n - 1][j];
    for (i = n - 1; i > 0; i--)
        for (j = 0; j <= i; j++) {
            if (s[i][j] > s[i][j + 1])
                s[i - 1][j] = s[i][j] + a[i - 1][j];
            else
                s[i - 1][j] = s[i][j + 1] + a[i - 1][j];
        }
    cout << s[0][0] << endl;
    return 0;
}