#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int p[300][2],flag=0,f[20][20];
int N,M,x2,y2;
int d[4][2]={{0,-1},{-1,0},{0,1},{1,0}};//左上右下
void mi(int x, int y , int n)
{
    int i;if(f[x][y]==0) return;
    if(x==x2&&y==y2)
    {
        flag++;
        for(i=0;i<n;i++)
        {
                printf("(%d,%d)->",p[i][0],p[i][1]);
        }
        printf("(%d,%d)\n",x2,y2);
    }

    for(i=0;i<4;i++)
    {
        f[x][y]=0;
        p[n][0]=x;
        p[n][1]=y;
        mi(x+d[i][0],y+d[i][1],n+1);
        f[x][y]=1;
    }
}
int main()
{
    int i,j,x1,y1;
    scanf("%d %d",&N,&M);
    memset(f,0,sizeof(f));
    memset(p,0,sizeof(p));
    for(i=1;i<=N;i++)
    {
        for(j=1;j<=M;j++)
            scanf("%d",&f[i][j]);
    }
    scanf("%d%d",&x1,&y1);
    scanf("%d %d",&x2,&y2);
    mi(x1,y1,0);
    if(flag==0)
        printf("-1");
    return 0;
}