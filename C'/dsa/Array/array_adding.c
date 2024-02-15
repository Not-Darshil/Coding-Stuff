//BASED ON INDEX

#include<stdio.h>
void main()
{
    int n,pos,ele,A[20],i;
    printf("enter number of elements");
    scanf("%d",&n);
    
    for(i=0;i<n;i++)
    {
        printf("Enter elemet:");
        scanf("%d",&A[i]);
    }
    printf("enter indexat which to be inserted at");
    scanf("%d",&pos);
    printf("enter the number you want to insert");
    scanf("%d",&ele);
    n++;
    for(i=n;i>pos-1;i--)
    {
        A[i]=A[i-1];
    }
    A[pos]=ele;
    for(i=0;i<n;i++)
    {
        printf("%d\n",A[i]);
    }
}