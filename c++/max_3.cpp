#include <iostream>
using namespace std;

int main() {
    int n1;
    cout<<"ENTER NO.1:";
    cin>>n1;

    int n2;
    cout<<"ENTER NO.2:";
    cin>>n2;

    int n3;
    cout<<"ENTER NO.3:";
    cin>>n3;

    if (n1>n2 && n1>n3){
        cout<<"NUMBER 1 IS BIGGEST:";
        cout<<n1<<"\n";
    }

    else if (n2>n1 && n2>n3){
        cout<<"NUMBER 2 IS BIGGEST:";
        cout<<n2<<"\n";
    }

    else {
        cout<<"NUMBER 3 IS BIGGEST:";
        cout<<n3<<"\n";
    }
    
return 0;
}