//ON BASES OF INDEX
// /*

#include<stdio.h>
void main()
{
int n,pos,A[20],i;
printf("enter number of elements:");
scanf("%d",&n);
for(i=0;i<n;i++)
{
    printf("Enter element:");
scanf("%d",&A[i]);
}
printf("enter index to be deleted at:");
scanf("%d",&pos);
for(i=pos;i<n-1;i++)
{
    A[i]=A[i+1];
}
printf("New Array: \n");
for(i=0;i<n-1;i++)
{
printf("%d \n",A[i]);
}
}
// */

//ON BASES OF ELEMENT
/*

#include<stdio.h>
void main()
{
int n,ele,A[20],i,j,new_num;
printf("Enter number of elements:");
scanf("%d",&n);
for(i=0;i<n;i++)
{
scanf("%d",&A[i]);
}
new_num=n;
printf("Enter Element to be deleted:");
scanf("%d",&ele);
for(i=0;i<n;i++)
{
    if (ele==A[i]){
        for(j=i;j<n-1;j++){
            A[j]=A[j+1];
        }
        new_num=new_num-1;

    }
}
printf("New Array: \n");
for(i=0;i<new_num;i++)
{
printf("%d \n",A[i]);
}
}
*/




