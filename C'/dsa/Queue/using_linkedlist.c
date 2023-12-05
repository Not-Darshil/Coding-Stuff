// Using LINKED LIST
#include<stdio.h>
#include<stdlib.h>
struct node
{
    int data;
    struct node *next;
};
void main()
{
    int ch,poped;
    struct node * top = NULL,*head,*P;
    do
    {
        printf(" 1:ENQUEUE \n 2:DEQUEUE \n 3:DISPLAY \n 4:EXIT\n");
        printf("Enter Choice[1,2,3,4]:");
        scanf("%d",&ch);    
        switch (ch)
        {
            case 1: if (head==NULL)
                {
                    head=(struct node *)malloc(sizeof(struct node));
                    printf("Enter Data:");
                    scanf("%d",&head->data);
                    head->next=NULL;
                    top=head;
                }
                else{
                    P=(struct node *)malloc(sizeof(struct node));
                    printf("Enter Data:");
                    scanf("%d",&P->data);
                    P->next=NULL;
                    top->next=P;
                    top=P;                 
                }
                break;
            case 2: if (head==NULL)
                {
                    printf("UNDERFLOW \n");
                }
                else{
                    P=head;
                    head=head->next;//head=null agr last element h to
                    poped=P->data;
                    free(P);
                    printf("DEQUEUED %d \n",poped);
                }      
                break;
            case 3: if (head==NULL)
                {
                    printf("EMPTY QUEUE\n");
                }
                else{
                    P=head;
                    while(P!=NULL)
                        {
                            printf("%d \n", P->data);
                            P=P->next;
                        }
                    printf("\n");
                }
                break;
            case 4:
                {
                    printf("EXITED\n");
                    break;
                }
            default: printf("unknown\n");
        }    
    }
    while(ch != 4);

}