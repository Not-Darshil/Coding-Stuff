#include<stdio.h>
#include<stdlib.h>
typedef struct node 
{
    int data;
    struct node *next;
}node;

void main()
{ 
    node *head=NULL,*P,*Q;
    int n,i,pos,ch,now;
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
    printf("1)Head \n2)End \n3)Middle \nEnter Choice:");
    scanf("%d",&ch);
    P=head;
    switch(ch)
    {
    case 1: Q=P->next;
            free(head);
            head=Q;
            break;
    case 2: P=head;
            while(P->next->next!=NULL)
            {
                P=P->next;
            }
            Q=P->next;
            free(Q);
            P->next=NULL;
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
    while(P!=NULL)
    {
        printf("%d -> \t",P->data);
        P=P->next;
    }
    printf("NULL \n");

}