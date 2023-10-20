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
    int ch;
    struct node * top = NULL,*p;
    do
    {
        printf("\n 1:PUSH \n 2:POP \n 3:DISPLAY \n 4:EXIT\n");
        printf("Enter Choice[1,2,3,4]:");
        scanf("%d",&ch);    
        switch (ch)
        {
            case 1: if (top==NULL)
                {
                    p=(struct node *)malloc(sizeof(struct node));
                    printf("Enter Data:");
                    scanf("%d",&p->data);
                    p->next=NULL;
                    top=p;
                }
                else{
                    p=(struct node *)malloc(sizeof(struct node));
                    printf("Enter Data:");
                    scanf("%d",&p->data);
                    p->next=top;
                    top=p;                 

                }
                break;
            case 2: if (top==NULL)
                {
                    printf("UNDERFLOW \n");
                }
                else{
                    p=top;
                    top=top->next;
                    free(p);
                    printf("POPPED\n");
                }      
                break;
            case 3: if (top==NULL)
                {
                    printf("EMPTY STACK\n");
                }
                else{
                    p=top;
                    while(p!=NULL)
                        {
                            printf("%d \n", p->data);
                            p=p->next;
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