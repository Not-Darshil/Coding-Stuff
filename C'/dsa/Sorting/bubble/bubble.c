#include <stdio.h>
void main()
{
    int A[10]={7,64,25,70,12,22,11,13},i,j,temp,n=8;
    printf("\nUNSORTED ARRAY : ");
    for(int i=0;i<n;i++)
    {
        printf("%d ",A[i]);
    }
    for(i=0;i<n;i++)
    {
        for (j=0;j<n-i-1;j++)
        {
            if(A[j]>A[j+1])
            {
                temp=A[j];
                A[j]=A[j+1];
                A[j+1]=temp;
            }
        }

    }


    printf("\nSORTED ARRAY : ");
    for(int i=0;i<n;i++)
    {
        printf("%d ",A[i]);
    }
}