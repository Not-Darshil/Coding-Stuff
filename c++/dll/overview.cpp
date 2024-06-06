#include<bits/stdc++.h>
using namespace std;

class Node{
    public:
    int data;
    Node *prev;
    Node *next;

    Node(int data1,Node *prev1,Node *next1){
        data = data1;
        prev=prev1; 
        next=next1;
    }

    Node(int data1,Node *prev1){
        data = data1;
        prev=prev1; 
        next=nullptr;
    }

    Node(int data1){
        data = data1;
        prev=nullptr;
        next=nullptr;
    }
};

int main(){
    vector<int>arr= {0,1,2,3};
    Node *head=new Node(arr[0]);
    Node*prev=nullptr;
    for(int i=1;i<arr.size();i++){
        Node *temp=new Node(arr[i],prev);
        prev->next=temp;
        prev=temp;
    }
    Node *temp=head;
    while(temp){
        cout<<temp->data<<"<-->";
        temp=temp->next;
    }
    return 0;
}