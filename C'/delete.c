#include <stdio.h>

int main() {
    int i,j,k=1,cnt=0,A[3][3];
    printf("Enter Normal Marix Elements:\n");
    for (i=0;i<3;i++)
    {
        for (j=0;j<3;j++)
        {
            scanf("%d",&A[i][j]);
        }
        printf("\n");
    }
        return 0;
}