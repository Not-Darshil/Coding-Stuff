#include<stdio.h>
#include<stdlib.h>
typedef struct cnode 
{
    int data;
    struct cnode *next;
}cnode;

void main()
{ 
    cnode *head=NULL,*P,*Q,*p;
    int n,i,pos,ch;
    printf("Enter No. of Nodes: ");
    scanf("%d",&n);
    head=(cnode *)malloc(sizeof(cnode));
    printf("Enter Value: ");
    scanf("%d",&head->data);
    head->next=head;
    P=head;
    for (i=0;i<n-1;i++)
    {
        Q=(cnode *)malloc(sizeof(cnode));
        printf("Enter Value: ");
        scanf("%d",&Q->data);
        Q->next=head;
        P->next=Q;
        P=Q;
    }
    P=head;
    while(P->next!=head){
        printf("%d -> \t",P->data);
        P=P->next;
    }
    printf("%d -> \t repeat -> \t",P->data);
    P=P->next;
    printf("%d",P->data);    
}