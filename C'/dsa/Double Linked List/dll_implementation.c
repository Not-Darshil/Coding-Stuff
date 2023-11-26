#include<stdio.h>
#include<stdlib.h>
typedef struct dnode 
{
    int data;
    struct dnode *prev;
    struct dnode *next;
}dnode;

void main()
{ 
    dnode *head=NULL,*P,*Q;
    int n,i;
    printf("Enter No. of Nodes: ");
    scanf("%d",&n);
    head=(dnode *)malloc(sizeof(dnode));
    printf("Enter Value: ");
    scanf("%d",&head->data);
    head->next=NULL;
    head->prev=NULL;
    P=head;
    for (i=0;i<n-1;i++)
    {
        Q=(dnode *)malloc(sizeof(dnode));
        printf("Enter Value: ");
        scanf("%d",&Q->data);
        Q->next=NULL;
        Q->prev=P;
        P->next=Q;
        P=Q;
    }
    P=head;
    while(P!=NULL){
        printf("%d <-> \t",P->data);
        P=P->next;
    }
    printf("NULL \n");
    
}