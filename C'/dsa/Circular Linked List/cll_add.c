#include<stdio.h>
#include<stdlib.h>
typedef struct cnode 
{
    int data;
    struct cnode *next;
}cnode;

void main()
{ 
    cnode *head=NULL,*P,*Q;
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
    printf("1)Head \n2)End \n3)Middle \nEnter Choice:");
    scanf("%d",&ch);
    switch(ch)
    {
    case 1: Q=(cnode *)malloc(sizeof(cnode));
            printf("Enter Value: ");
            scanf("%d",&Q->data);
            Q->next=head;
            while(P->next!=head)
            {
                P=P->next;
            }
            P->next=Q;
            head=Q;
            break;
    case 2: Q=(cnode *)malloc(sizeof(cnode));
            printf("Enter Value: ");
            scanf("%d",&Q->data);
            Q->next=head;
            while(P->next!=head)
            {
                P=P->next;
            }
            P->next=Q;
            break;
    case 3: Q=(cnode *)malloc(sizeof(cnode));
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
            Q->next=P->next;
            P->next=Q;
            break;
    default: printf("wrong choice");
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