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
    struct node * top = NULL,*P;
    do
    {
        printf(" 1:PUSH \n 2:POP \n 3:DISPLAY \n 4:EXIT\n");
        printf("Enter Choice[1,2,3,4]:");
        scanf("%d",&ch);    
        switch (ch)
        {
            case 1: if (top==NULL)
                {
                    P=(struct node *)malloc(sizeof(struct node));
                    printf("Enter Data:");
                    scanf("%d",&P->data);
                    P->next=NULL;
                    top=P;
                }
                else{
                    P=(struct node *)malloc(sizeof(struct node));
                    printf("Enter Data:");
                    scanf("%d",&P->data);
                    P->next=top;
                    top=P;                 

                }
                break;
            case 2: if (top==NULL)
                {
                    printf("UNDERFLOW \n");
                }
                else{
                    P=top;
                    top=top->next;//top=null agr last element h to
                    poped=P->data;
                    free(P);
                    printf("POPPED %d",poped);
                }      
                break;
            case 3: if (top==NULL)
                {
                    printf("EMPTY STACK\n");
                }
                else{
                    P=top;
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