#include<stdio.h>
void main()
{
    int A[10]={10,11,12,13,14,15,16,17,18,19},u=9,l=0,mid,key;
    for (int i=0;i<10;i++)
    {
        printf("%d ", A[i]);
    }
    printf("\n Enter Element to be searched:");
    scanf("%d",&key);
    mid=(u+l)/2;
    while(u>=l && A[mid]!=key)
    {
        mid=(u+l)/2;
        if (A[mid]==key)
        {
            printf("Found at %d", mid);
            break;
        }
        else
        {
            if (A[mid]<key)
            {
                l=mid+1;
            }
            else
            {
                u=mid-1;
            }
        }
    }
    if (u<=l && A[mid]!=key)
    {
        printf("Not Found");
    }
}