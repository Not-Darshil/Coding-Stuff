#include <stdio.h>
int main(){
    int i,j,cnt=0,A[3][3]={0},k;
    printf("Enter No. of Non Zeroes Elements:");
    scanf("%d",&cnt);
    int B[cnt][3];
    printf("Enter Sparse Marix Elements in proper order:\n");
    for (i=0;i<cnt;i++)
    {
        printf("\nRow Value:");
        scanf("%d",&B[i][0]);
        printf("Column Value:");
        scanf("%d",&B[i][1]);
        printf("Value:");
        scanf("%d",&B[i][2]);
    }
    for (i=0;i<cnt;i++)
    {
        for (j=0;j<3;j++)
        {
            printf(" %d ",B[i][j]); 
        }
        printf("\n");
    }
    k=0;
    for (k=0;k<cnt;k++)
    {
        i=B[k][0];
        j=B[k][1];
        A[i][j]=B[k][2];
        printf("\n");
    }
    printf("Normal Marix:\n");
    for (i=0;i<3;i++)
    {
        for (j=0;j<3;j++)
        {
            printf("%d ",A[i][j]);
        }
        printf("\n");
    }

    return 0;
}