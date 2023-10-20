//WAP TO PRINT THE SUM OF UPPER TRIANGULAR MATRIX
// #include<stdio.h>
// void main()
// {
//     int i,j,n,sum=0,A[10][10];
//     printf("Enter no.of rows and columns:");
//     scanf("%d",&n);
//     printf("Enter Elements:");
//     for (i=0;i<n;i++)
//     {
//         for (j=0;j<n;j++)
//         {
//             scanf("%d",&A[i][j]);
//         }
//     }
//     for (i=0;i<n;i++)
//     {
//         for (j=0;j<n;j++)
//         {
//             printf("%d",A[i][j]);
//         }
//         printf("\n");
//     }
//     for (i=0;i<n;i++)
//     {
//         for (j=0;j<n;j++)
//         {
//             if(i<=j){
//                 sum +=A[i][j];
//             }

//         }
//     }
//     printf("\n");
//     printf("SUM: %d\n",sum);
    
// }

//program 2b:WAP TO PRINT THE SUM OF LOWER TRIANGULAR MATRIX
// #include<stdio.h>
// void main()
// {
//     int i,j,n,sum=0,A[10][10];
//     printf("Enter no.of rows and columns:");
//     scanf("%d",&n);
//     printf("Enter Elements:");
//     for (i=0;i<n;i++)
//     {
//         for (j=0;j<n;j++)
//         {
//             scanf("%d",&A[i][j]);
//         }
//     }
//     for (i=0;i<n;i++)
//     {
//         for (j=0;j<n;j++)
//         {
//             printf("%d",A[i][j]);
//             if(i>=j){
//                 sum +=A[i][j];
//             }
//         }
//         printf("\n");
//     }
//     printf("\n");
//     printf("SUM: %d\n",sum);
    
// }

// WAP TO FIND THE SUM OF THE DIAGONAL ELEMENT OF THE MATRIX
// #include<stdio.h>
// void main()
// {
//     int i,j,n,sum=0,A[10][10];
//     printf("Enter no.of rows and columns:");
//     scanf("%d",&n);
//     printf("Enter Elements:");
//     for (i=0;i<n;i++)
//     {
//         for (j=0;j<n;j++)
//         {
//             scanf("%d",&A[i][j]);
//         }
//     }
//     for (i=0;i<n;i++)
//     {
//         for (j=0;j<n;j++)
//         {
//             printf("%d",A[i][j]);
//             if(i==j){
//                 sum +=A[i][j];
//             }
//         }
//         printf("\n");
//     }
//     printf("\n SUM: %d\n",sum);
    
// }

//WAP TO FIND THE SUM OF THE Z SHAPED MATRIX 
// #include<stdio.h>
// void main()
// {
//     int i,j,n,sum=0,A[10][10];
//     printf("Enter no.of rows and columns:");
//     scanf("%d",&n);
//     printf("Enter Elements:");
//     for (i=0;i<n;i++)
//     {
//         for (j=0;j<n;j++)
//         {
//             scanf("%d",&A[i][j]);
//         }
//     }
//     for (i=0;i<n;i++)
//     {
//         for (j=0;j<n;j++)
//         {
//             printf("%d",A[i][j]);
//             if(i==0 || i==n-1 || i+j==n-1){
//                 sum +=A[i][j];
//             }
//         }
//         printf("\n");
//     }
//     printf("\n SUM: %d\n",sum);
    
// }

// WAP TO FIND THE SUM OF X SHAPED MATRIX ELEMENTS
#include<stdio.h>
void main()
{
    int i,j,n,sum=0,A[10][10];
    printf("Enter no.of rows and columns:");
    scanf("%d",&n);
    printf("Enter Elements:");
    for (i=0;i<n;i++)
    {
        for (j=0;j<n;j++)
        {
            scanf("%d",&A[i][j]);
        }
    }
    for (i=0;i<n;i++)
    {
        for (j=0;j<n;j++)
        {
            printf("%d",A[i][j]);
            if(i==j || i+j==n-1){
                sum +=A[i][j];
            }
        }
        printf("\n");
    }
        printf("\n SUM: %d\n",sum);
    
}
