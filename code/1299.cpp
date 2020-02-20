#include <bits/stdc++.h>
#include <algorithm>
#include <iostream>
#include <cstdio>
#include <cmath>
#include<iomanip>
#include<cstring>
#include <algorithm>
#include <sstream>

#define ll long long
#define INF 0x3f3f3f3f
using namespace std;

const int N = 1e3 + 10;
int dp[N];
int a[N];

int main() {
    int n;
    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> a[i];
        dp[i] = INF;
    }
    dp[0] = a[0];
    int pos = 0;
    for (int i = 1; i < n; i++) {
        if (a[i] > dp[pos]) {
            dp[++pos] = a[i];
        } else {
            int k = lower_bound(dp, dp + pos, a[i]) - dp;
            dp[k] = a[i];
        }

    }

    cout << pos + 1 << endl;
    return 0;
}