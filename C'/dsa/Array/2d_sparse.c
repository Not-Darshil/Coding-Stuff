#include <stdio.h>
int main(){
    int i,j,k=0,cnt=0,A[3][3];
    printf("Enter Normal Marix Elements:\n");
    for (i=0;i<3;i++)
    {
        for (j=0;j<3;j++)
        {
            scanf("%d",&A[i][j]);
        }
        printf("\n");
    }
    for (i=0;i<3;i++)
    {
        for (j=0;j<3;j++)
        {
            printf("%d ",A[i][j]);
        }
        printf("\n");
    }
    for (i=0;i<3;i++)
    {
        for (j=0;j<3;j++)
        {
            if (A[i][j]!=0){
                cnt++;}
        }
    }
    printf("cnt = %d",cnt);
    int B[cnt][3];
    for (i=0;i<3;i++){
        for (j=0;j<3;j++)
        { if (A[i][j] != 0)
            {               
                B[k][0]=i;
                B[k][1]=j;
                B[k][2]=A[i][j];
                k++;
            }
        }
        printf("\n");
    }
    printf("Sparse Marix:\n");
    for (i=0;i<cnt;i++){
        for (j=0;j<3;j++){
            printf(" %d ",B[i][j]); 
        }
        printf("\n");
    }

    return 0;
}