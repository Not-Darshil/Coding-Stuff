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
    int n,i,pos,ch,now;
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
    scanf("%d",&ch);    switch(ch)
    {
    case 1: Q=P->next;
            while(P->next!=head)
            {
                P=P->next;
            }
            P->next=head->next;
            free(head);
            head=Q;
            break;
    case 2: while(P->next->next!=head)
            {
                P=P->next;
            }
            Q=P->next;
            free(Q);
            P->next=head;
            break;
    case 3: printf("Enter Position: ");
            scanf("%d",&pos);
            now=0;
            while(now<pos-1){
                P=P->next;
                now++;
            }
            Q=P->next;
            P->next=Q->next;
            free(Q);
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