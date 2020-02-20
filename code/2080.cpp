#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int main()
{
    char X[510], Y[510];
    int  c[510][510]={0,};
    while(scanf("%s %s",X,Y)!=EOF){
        int i,j,x,y;
        x=strlen(X);
        y=strlen(Y);
        for(i=0; i<=x; i++)
            c[i][0]=0;
        for(j=0; j<=y; j++)
            c[0][j]=0;
        for(i=1; i<=x; i++){
            for(j=1; j<=y; j++){
                if(X[i-1]==Y[j-1])
                    c[i][j]=c[i-1][j-1]+1;
                else{
                    if(c[i-1][j]>c[i][j-1]){
                        c[i][j]=c[i-1][j];
                    }
                    else c[i][j]=c[i][j-1];
                }
            }
        }
        printf("%d\n",c[x][y]);



    }

    return 0;
}