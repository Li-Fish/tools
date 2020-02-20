#include <stdio.h>
#include <stdlib.h>
int a[101][101],b[101][101];
int main()
{
    int i,j,n;
    while(~scanf("%d",&n))
    {
        for(i=1; i<=n; i++)
            for(j=1; j<=i; j++)
                scanf("%d",&b[i][j]);
        for(j=1; j<=n; j++)
            a[n][j]=b[n][j];
        for(i=n-1; i>=1; i--)
            for(j=1; j<=i; j++)
            {
                if(a[i+1][j+1]<a[i+1][j])
                    a[i][j]=a[i+1][j+1]+b[i][j];
                else
                    a[i][j]=a[i+1][j]+b[i][j];
            }
        printf("%d\n",a[1][1]);
    }
    return 0;
}