#include<stdio.h>
void main()
{
    int ch=0,ele,del,top=-1,i,size=10;
    int stack[size];
    while(ch!=4){
        printf("\n 1:PUSH \n 2:POP \n 3:DISPLAY \n 4:EXIT\n");
        printf("Enter Choice[1,2,3,4]:");
        scanf("%d",&ch);    
        switch (ch)
        {
            case 1: if (top==size-1)
                {
                    printf("OVERFLOW\n");
                }
                else{
                    printf("Enter Data:");
                    scanf("%d",&ele);
                    top++;                
                    stack[top]=ele;

                }
                break;
            case 2: if (top==-1)
                {
                    printf("UNDERFLOW \n");
                }
                else{
                    del=stack[top];
                    top--;
                    printf("POPPED :%d \n",del);
                }      
                break;
            case 3: if (top==-1)
                {
                    printf("EMPTY STACK\n");
                }
                else{
                    for(i=0;i<top+1;i++)
                    {
                        printf("%d\n",stack[i]);   
                    }
                }
                break;
            case 4: printf("EXITED\n");
                    break;
            default: printf("unknown\n");
        }    
    }
}