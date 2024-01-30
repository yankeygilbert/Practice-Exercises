//linked list implementation. c++ style using classes

#include <iostream>
class node{
   public:
        int val;
        node *pointertonext; 
        node *head = NULL ,*tail;      
};
class linkedlist: protected node{
    public:
        node *newnode;
        void insert(int);
        void print();
        void reverse();
};
void linkedlist::reverse(){
     node *cnode,*prevnode,*nxtnode;
     prevnode = NULL;
     cnode = head;
     while(cnode!=NULL){
        nxtnode = cnode->pointertonext;
        cnode->pointertonext = prevnode;
        prevnode = cnode;
        cnode = nxtnode;
     }
     node* nhead = tail;
     tail = head;
     head = nhead;
     std::cout << "reversing" <<std::endl;
     node *current = head;
    while (current != NULL){
        std::cout << current->val << " ";
        current = current->pointertonext;
    }
}
void linkedlist::insert(int value){
    newnode = new node;
    newnode->val = value;
    newnode->pointertonext = NULL;
    if(head == NULL){
        head = newnode; 
        tail = newnode;
    }
    else{
        tail->pointertonext = newnode;
        tail = newnode;
    }   
}
void linkedlist:: print(){
   node *current = head;
    while (current != NULL){
        std::cout << current->val << " ";
        current = current->pointertonext;
    }
}
main(){
    linkedlist list1 ;
    linkedlist list2;
    list1.insert(4);
    list1.insert(2);
    list1.insert(7);
    list1.insert(12);
    list1.print();
    std::cout<<std::endl;
    list2.insert(94);
    list2.insert(5);
    list2.insert(3);
    list2.insert(7);
    list2.print();   
}

