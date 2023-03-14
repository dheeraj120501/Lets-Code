/*
Implement Linked List
Linked List ADT
1. Insert: inserts an element into the list
2. Delete: removes and returns the specified position element from the list
3. Delete List: removes all elements of the list (disposes the list)
4. Count: returns the number of elements in the list
5. Find nth node from the end of the list
*/
#include <iostream>
using namespace std;

template <class T>
struct Node {
    T data;
    Node<T>* next;

    Node(T data) {
        this->data = data;
        next = nullptr;
    }
};

template <class T>
class LL {
    Node<T>* head;
    int count;
    public:
    LL(int n) {
        if(n==0){
            head = nullptr;
            count = 0;
        } else {
            try {
                if(n<0){
                    throw -1;
                }
                T data;
                cout<<"Enter the data for the node: ";
                cin>>data;
                Node<T>* prev = new Node<T>(data);
                head = prev;
                n--;
                while(n--) {
                    cout<<"Enter the data for the node: ";
                    cin>>data;
                    Node<T>* temp = new Node<T>(data);
                    prev->next = temp;
                    prev = temp;
                }   
            }
            catch(int e) {
                if(e == -1)
                cout<<"Can't have negitive size\n";
            }
        }
    }
    
    LL(): LL(0) {
    }
    
    void insert(int pos, T data) {
        Node<T>* temp = new Node<T>(data);
        if(pos == 0) {
            temp->next = head;
            head = temp;
            count++;
            return;
        }
        try {
            if(pos > count) {
                throw 1;
            }
            else if(pos<0){
                throw -1;
            }
            Node<T>* prev = head;
            while(--pos) {
                prev = prev->next;
            }
            temp->next = prev->next;
            prev->next = temp;
            count++;
        } catch(int e) {
            if(e == -1)
            cout<<"Insertion position can't be negitive\n";
            else if(e == 1)
            cout<<"Can't insert at the position that is not available in linked list\n";
        }
    }

    void print(int idx = -1) {
        Node<T>* temp = head;
        if(idx == -1) {
            while(temp != nullptr) {
                cout<<temp->data<<" ";
                temp = temp->next;
            }
            cout<<endl;
            return;
        }
        try {
            if(idx<-1) {
                throw -1;
            }
            if(idx >= count) {
                throw 1;
            }
            while(idx--){
                temp = temp->next;
            }
            cout<<temp->data<<endl;
        }
        catch(int e) {
            if(e == -1)
            cout<<"Index can't be negitive\n";
            else if(e == 1)
            cout<<"Index can't be greater than the size of linked list\n";
        }
    }

    int size() const {
        return count;
    }

    bool search(T data) {
        Node<T>* temp = head;
        try{
            if(temp == nullptr){
                throw 0;
            }
            while(temp != nullptr) {
                if(temp->data == data){
                    return true;
                }
                temp = temp->next;
            }
        }catch(int e) {
            if(e == 0) {
                cout<<"Can't search in a empty Linked List\n";
            }
        }
        return false;
    }

};

int main() {
    LL<int> l;
    l.insert(2, 10);
    l.insert(0, 4);
    l.print();
    cout<<l.search(1)<<endl;
    cout<<l.search(4)<<endl;
    // for(int i=0; i<l.size(); i++) {
    //     l.print(i);
    // }
}