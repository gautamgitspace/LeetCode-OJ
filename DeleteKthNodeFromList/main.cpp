//
//  main.cpp
//  CTCI2_2
//
//  Created by Gautam on 11/2/16.
//  Copyright © 2016 Gautam. All rights reserved.
//
// kth to last element - USING TWO PTRs
#include <iostream>
#include "LinkedList.h"

using namespace std;

LinkedList::LinkedList()
{
    this->head = nullptr;
}

LinkedList::~LinkedList()
{
    Node* current = head;
    
    while (current != 0)
    {
        Node* next = current->next;
        delete current;
        current = next;
    }
    
    head = nullptr;
    
    std::cout << "List successfully deleted from memory" << std::endl;
}

Node* LinkedList::ktoLast(Node* head, int k)
{
    Node *ptr1=head;
    Node *ptr2=head;
    
    for(int i=0;i<k;i++)
    {
        /*MOVE PTR2 TILL K*/
        if(ptr2==nullptr)
            cout<<"EMPTY LIST"<<endl;
        ptr2 = ptr2->next;
    }
    if(ptr2==nullptr)
        cout<<"REACHED END"<<endl;
    while(ptr2!=nullptr)
    {
        /*NOW PTR2 WILL HIT THE END AFTER LEN-K STEP and AT THAT TIME PTR1 WILL ALSO COVER LEN-K*/
        ptr1 = ptr1->next;
        ptr2 = ptr2->next;
    }
    return ptr1;
}

void LinkedList::insert(int value)
{
    if (head == NULL)
    {
        head = new Node();
        tail = head;
        head->next = nullptr;
        head->data = value;
    }
    else
    {
        tail->next = new Node();
        tail = tail->next;
        tail->data = value;
        tail->next = nullptr;
    }
}

void LinkedList::deleteKthLastNode(Node* ptr)
{
    Node *s = head;
    Node *prev = head;
    while(s->next!=ptr->next)
    {
        prev = s;
        s = s->next;
    }
    /*NOW PREV WILL HAVE THE PREVIOUS*/
    prev->next = ptr->next;
}

void LinkedList::display()
{
    Node* temp;
    
    if (head == NULL)
    {
        return;
    }
    
    temp = head;
    
    while (temp != NULL)
    {
        std::cout << temp->data << ' ';
        temp = temp->next;
    }
    
    std::cout << std::endl;
}


int main(int argc, const char * argv[])
{
    LinkedList linkedlist = *new LinkedList();
    linkedlist.insert(10);
    linkedlist.insert(12);
    linkedlist.insert(14);
    linkedlist.insert(16);
    linkedlist.insert(18);
    linkedlist.insert(20);
    linkedlist.insert(10);
    
    linkedlist.display();
    cout<<"Kth to Last: "<<linkedlist.ktoLast(linkedlist.head, 3)->data<<endl;
    cout<<"Attempting to delete Kth to Last"<<endl;
    linkedlist.deleteKthLastNode(linkedlist.ktoLast(linkedlist.head, 3));
    linkedlist.display();
    
        return 0;
}
