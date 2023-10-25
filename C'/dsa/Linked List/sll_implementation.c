#include<stdio.h>
#include<stdlib.h>
typedef struct node 
{
    int data;
    struct node *next;
}node;

void main()
{ 
    node *head=NULL,*P,*Q,*p;
    int n,i;
    printf("Enter No. of Nodes: ");
    scanf("%d",&n);
    head=(node *)malloc(sizeof(node));
    printf("Enter Value: ");
    scanf("%d",&head->data);
    head->next=NULL;
    P=head;
    for (i=0;i<n-1;i++)
    {
        Q=(node *)malloc(sizeof(node));
        printf("Enter Value: ");
        scanf("%d",&Q->data);
        Q->next=NULL;
        P->next=Q;
        P=Q;
    }
    P=head;
    while(P!=NULL){
        printf("%d -> \t",P->data);
        P=P->next;
    }
    printf("NULL \n");
    
}