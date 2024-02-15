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
    dnode *head=NULL,*P,*Q,*R;
    int n,i,pos,ch;
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
    printf("1)Head \n2)End \n3)Middle \nEnter Choice:");
    scanf("%d",&ch);
    switch(ch)
    {
    case 1: Q=(dnode *)malloc(sizeof(dnode));
            printf("Enter Value: ");
            scanf("%d",&Q->data);
            Q->prev=NULL;
            Q->next=P;
            P->prev=Q;
            head=Q;
            break;
    case 2: Q=(dnode *)malloc(sizeof(dnode));
            printf("Enter Value: ");
            scanf("%d",&Q->data);
            Q->next=NULL;
            while(P->next!=NULL)
            {
                P=P->next;
            }
            Q->prev=P;
            P->next=Q;
            break;
    case 3: Q=(dnode *)malloc(sizeof(dnode));
            printf("Enter Position: ");
            scanf("%d",&pos);
            printf("Enter Value: ");
            scanf("%d",&Q->data);
            i=0;
            while(i<pos-1)
            {
                P=P->next;
                i++;
            }
            R=P->next;
            P->next=Q;
            Q->prev=P;
            Q->next=R;
            R->prev=Q;
            break;
    default: printf("wrong choice");
    }
    P=head;
    while(P!=NULL)
    {
        printf("%d <-> \t",P->data);
        P=P->next;
    }
    printf("NULL \n");

}