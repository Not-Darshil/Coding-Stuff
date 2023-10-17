#include<stdio.h>
void main(){
    int A[20],B[20],C[40],i,j,k,n,m;
    printf("enter number of elements of A array");
    scanf("%d",&n);
    for(i=0;i<=n-1;i++){
        scanf("%d",&A[i]);
    }
    printf("enter number of elements of B array");
    scanf("%d",&m);
    for(j=0;j<=m-1;j++)
    {
    scanf("%d",&B[j]);
    }
    i=j=k=0;
    while (i<=n-1 && j<=m-1)
    {
        if (A[i]<=B[j]){
            C[k]=A[i];
            i++;
            k++;
        }
        else{
            C[k]=B[j];
            j++;
            k++;
        }
    }
    while(i<=n-1){
        C[k]=A[i];
        i++;
        k++;
        }
    while(j<=m-1){
        C[k]=B[j];
        j++;
        k++;
        }
    printf("\n");   
    for (k=0; k<=n+m-1; k++)
    {
        printf("%d \n",C[k]);

    }
}