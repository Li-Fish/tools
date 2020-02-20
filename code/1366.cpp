#include <stdio.h>
#include <string.h>
#include <math.h>
int p[100001][20];
int max1(int a,int b)
{
    return (a>b)?a:b;
}
int max2(int a,int b,int c)
{
    int max=(a>b)?a:b;
    return (max>c)?max:c;
}
int f(int maxtime)
{
    int i,j;
    for(i=maxtime-1;i>=0;--i)
    {
        p[i][0]=max1(p[i+1][0],p[i+1][1])+p[i][0];
        for(j=1;j<10;++j)
        {
            p[i][j]=max2(p[i+1][j-1],p[i+1][j],p[i+1][j+1])+p[i][j];
        }
        p[i][10]=max1(p[i+1][10],p[i+1][9])+p[i][10];
    }
    return p[0][5];
}
int main()
{
    int i,m,time,maxtime,location;
    while(~scanf("%d",&m)&&m)
    {
        memset(p,0,sizeof(p));
        maxtime=-1;
        for(i=1;i<=m;i++)
        {
            scanf("%d%d",&location,&time);
            ++p[time][location];
            if(time>maxtime)
                maxtime=time;
        }
        printf("%d\n",f(maxtime));
    }
    return 0;
}