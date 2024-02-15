#include<stdio.h>
void main()
{
    int A[10]={7,64,25,70,12,22,11,13},i=0,j,n=8,temp,min_index;
    printf("\nUNSORTED ARRAY : ");
    for(int i=0;i<n;i++)
    {
        printf("%d ",A[i]);
    }
    for(int i=0;i<n-1;i++)
    {
        min_index=i;
        for(j=i+1;j<n;j++)//j<n-1
        {
            if (A[j]<A[min_index])
            {
                min_index=j;
            }
        }
        //swap min_index with i
        temp=A[min_index];
        A[min_index]=A[i];
        A[i]=temp;
    }
    printf("\nSORTED ARRAY : ");
    for(int i=0;i<n;i++)
    {
        printf("%d ",A[i]);
    }

}