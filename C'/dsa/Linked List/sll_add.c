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
    int n,i,pos,ch;
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
    // P=head;
    // while(P!=NULL)
    // {
    //     printf("%d -> \t",P->data);
    //     P=P->next;
    // }
    // printf("NULL \n");

    P=head;
    printf("1)Head \n2)End \n3)Middle \nEnter Choice:");
    scanf("%d",&ch);
    switch(ch)
    {
    case 1: Q=(node *)malloc(sizeof(node));
            printf("Enter Value: ");
            scanf("%d",&Q->data);
            Q->next=head;
            head=Q;
            break;
    case 2: Q=(node *)malloc(sizeof(node));
            printf("Enter Value: ");
            scanf("%d",&Q->data);
            Q->next=NULL;
            while(P->next!=NULL)
            {
                P=P->next;
            }
            P->next=Q;
            break;
    case 3: Q=(node *)malloc(sizeof(node));
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
    while(P!=NULL)
    {
        printf("%d -> \t",P->data);
        P=P->next;
    }
    printf("NULL \n");

}