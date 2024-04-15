#include <iostream>
using namespace std;
void printsqr(n)
{
    for (int i = 0; i <n; i++)
    {
        for(int j = 0; j <i+1; j++)
        {
            cout << "*";
        }
    }
    for (int i = 1; i <n; i++)
    {
        for(int j = 0; j <i+1; j++)
        {
            cout << "*";
        }
    }
}

void main() {
    int i;
    cout << "eter";
    cin>>i;
    printsqr(i);
}
