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
    struct node * rear = NULL,*front =NULL,*P;
    do
    {
        printf(" 1:ENQUEUE \n 2:DEQUEUE \n 3:DISPLAY \n 4:EXIT\n");
        printf("Enter Choice[1,2,3,4]:");
        scanf("%d",&ch);    
        switch (ch)
        {
            case 1: if (front==NULL)
                {
                    front=(struct node *)malloc(sizeof(struct node));
                    printf("Enter Data:");
                    scanf("%d",&front->data);
                    front->next=front;
                    rear=front;
                }
                else
                {
                    P=(struct node *)malloc(sizeof(struct node));
                    printf("Enter Data:");
                    scanf("%d",&P->data);
                    P->next=front;
                    rear->next=P;
                    rear=P;                 
                }
                break;
            case 2: if (front==NULL)
                {
                    printf("UNDERFLOW \n");
                }
                else
                {
                    P=front;
                    front=front->next;//front=front agr last element h to
                    if (front==P)//Becuase if there is a last elemetnt in circ. queue then front-next is front itself therefore removing a last element should make the front A NULL value
                    {
                        front=NULL;
                    }
                    poped=P->data;
                    free(P);
                    printf("DEQUEUED %d \n",poped);
                }      
                break;
            case 3: if (front==NULL)
                {
                    printf("EMPTY QUEUE\n");
                }
                else{
                    P=front;
                    do
                    {
                        printf("%d \n", P->data);
                        P=P->next;
                    }
                    while(P!=rear->next);
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