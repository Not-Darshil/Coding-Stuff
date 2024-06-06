#include<bits/stdc++.h>
using namespace std;
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
    vector<int> arr={0,1,2,3,4,5,6,7,8,9};
    Node * head=new Node(arr[0]);
    Node *p=head;
    for(int i=1;i<arr.size();i++){
        Node * q= new Node(arr[i]);
        p->next=q;
        p=q;
    }

    //we can use either free or delete method 
    return 0;
} 