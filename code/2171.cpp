#include <stdio.h>
#include <stdlib.h>
#define N 1100

int main()
{
    int n;
    while(~scanf("%d", &n))
    {
        int max;
        int a[N], sum[N] = {0,};
        int i, j;
        scanf("%d", &a[0]);
        sum[0] = a[0];
        for(i=1; i<n; i++)
        {
            scanf("%d", &a[i]);
            sum[i] = a[i];
            max = 0;
            for(j=0; j<i; j++)
            {
                if(a[j] < a[i] && sum[j] > max)
                {
                    max = sum[j];
                }
            }
            sum[i] = a[i] + max;
        }
        max = 0;
        for(i=0; i<n; i++)
        {
            if(sum[i] > max)
            {
                max = sum[i];
            }

        }
        printf("%d\n", max);
    }
    return 0;
}