#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define max2(a,b) ((a) > (b) ? (a) : (b))
#define min2(a,b) ((a) < (b) ? (a) : (b))

char s[105][105];
int len[105];
int dp[30005];
int n;
int LCS(int *x)
{
    int a,i,j,b;

    for(i=1; i<=n; i++)
    {
        if(x[i]==0)
        {
            return 0;
        }

    }
    for(a=x[n]-1,i=n-1; i>=1; i--)
    {
        a=a*len[i]+x[i]-1;

    }
    if(dp[a]>=0)
    {
        return dp[a];

    }
    for(i=2; i<=n; i++)
    {
        if(s[1][x[1]-1]!=s[i][x[i]-1])
        {
            break;
        }
    }
    if(i>n)
    {
        for(j=1; j<=n; j++)
        {
            x[j]--;
        }
        b=LCS(x)+1;
        for(j=1; j<=n; j++)
        {
            x[j]++;
        }
    }
    else
    {
        b=0;
        for(j=1; j<=n; j++)
        {
            x[j]--;
            int t=LCS(x);
            b=max2(t,b);
            x[j]++;
        }
    }
    dp[a]=b;
    return b;
}
int main()
{
    int t,i;
    int m[105];
    scanf("%d",&t);
    while(t--)
    {
        scanf("%d",&n);
        for(i=1; i<=n; i++)
        {
            scanf("%s",s[i]);
            len[i]=m[i]=strlen(s[i]);
        }
        memset(dp,-1,sizeof(dp));
        printf("%d\n",LCS(m));
    }
    return 0;
}