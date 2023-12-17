#include<stdio.h>
void TOH(int,char,char,char);
void main()
{
    int N;
    printf(" Enter No. of Disks at A :");
    scanf("%d", &N);
    TOH(N,'A','B','C');
}
void TOH(int N,char P,char Q,char R)
{
    if (N>0)
    {
        TOH(N-1,P,R,Q);//qsr
        printf("%c to %c \n",P,R);//qs
        TOH(N-1,Q,P,R);//rqs
    }
    // return 0;
}
