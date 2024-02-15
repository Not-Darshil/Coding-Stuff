#include<stdio.h>
void main()
{
    int A[10]={10,11,12,13,10,15,16,17,10,19},key,i,flag=0;
    for (int i=0;i<10;i++)
    {
        printf("%d ", A[i]);
    }
    printf("\nEnter the element to be searched:");
    scanf("%d",&key);
    for (int i=0;i<10;i++)
    {
        if (A[i]==key)
        {
            flag=1;
            printf("Found at %d \n", i);
        }
    }
    if (flag==0)
    {
        printf("Not found");
    }

    
}