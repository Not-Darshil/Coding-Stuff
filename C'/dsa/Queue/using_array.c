#include<stdio.h>
void main()
{
    int ch=0,data,del,end=-1,i,size=10;
    int queue[size];
    while(ch!=4){
        printf(" 1:ENQUEUE \n 2:DEQUEUE \n 3:DISPLAY \n 4:EXIT\n");
        printf("Enter Choice[1,2,3,4]:");
        scanf("%d",&ch);    
        switch (ch)
        {
            case 1: if (end==size-1)
                {
                    printf("OVERFLOW\n");
                }
                else{
                    printf("Enter Data:");
                    scanf("%d",&data);
                    end++;                
                    queue[end]=data;

                }
                break;
            case 2: if (end==-1)
                {
                    printf("UNDERFLOW \n");
                }
                else{
                    del=queue[0];
                    for (i=0;i<end;i++)
                    {
                        queue[i]=queue[i+1];
                    }
                    end--;                    
                    printf("DEQUEUED :%d \n",del);
                }      
                break;
            case 3: if (end==-1)
                {
                    printf("EMPTY QUEUE\n");
                }
                else{
                    for(i=0;i<end+1;i++)
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