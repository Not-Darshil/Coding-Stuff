#include<stdio.h>
void main()
{
    int ch=0,data,del,front=-1,rear=-1,i,size=10;
    int queue[size];
    while(ch!=4){
        printf(" 1:ENQUEUE \n 2:DEQUEUE \n 3:DISPLAY \n 4:EXIT\n");
        printf("Enter Choice[1,2,3,4]:");
        scanf("%d",&ch);    
        switch (ch)
        {
            case 1: if (rear==size-1)
                {
                    printf("OVERFLOW\n");
                }
                else{
                    if (front==-1)
                    {
                        front=0;
                    }
                    printf("Enter Data:");
                    scanf("%d",&data);
                    rear++;                
                    queue[rear]=data;

                }
                break;
            case 2: if (rear==-1)
                {
                    printf("UNDERFLOW \n");
                }
                else{
                    del=queue[0];
                    if(rear==0)
                    {
                        front=-1;
                    }
                    for (i=0;i<rear;i++)
                    {
                        queue[i]=queue[i+1];
                    }
                    rear--;                    
                    printf("DEQUEUED :%d \n",del);
                }      
                break;
            case 3: if (rear==-1)
                {
                    printf("EMPTY QUEUE\n");
                }
                else{
                    for(i=0;i<rear+1;i++)
                    {
                        printf("%d\n",queue[i]);   
                    }
                }
                break;
            case 4: printf("EXITED\n");
                    break;
            default: printf("unknown\n");
        }    
    }
}