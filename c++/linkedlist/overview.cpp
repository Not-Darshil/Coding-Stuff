#include<bits/stdc++.h>
using namespace std;
//with struct you dont have concepts of OOPS
class Node{
    public:
    int data;
    Node*next;
    
    public:
    Node(int data1,Node* next1){
        data=data1;
        next=next1;
    }

    public:
    Node(int data1){
        data=data1;
        next=nullptr;
    }
};


int main(){
    vector<int> arr={1,2,3,4,5};
    Node *y= new Node(arr[0],nullptr);//it gives the pointer to the object
    cout<<y->data;
    // Not used these
    // Node x= Node(2,nullptr);
    // Node *y =&x;
    return 0;
}

