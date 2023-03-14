/*
Problem: Give an algorithm for finding maximum element in binary tree.
*/

#include <bits/stdc++.h>
using namespace std;

class Node{
    public:
    int data;
    Node* left;
    Node* right;
    Node(int val) {
        data = val;
        left = right = nullptr;
    } 
};

void displayNode(Node* node) {
    cout<<node->data<<endl;
}

// Time Complexity: O(n) Space Complexity: O(n)
Node* maxElementRecc(Node* root) {

    if(root == nullptr) {
        Node* temp = new Node(INT_MIN); 
        return temp;
    }

    Node* lmax = maxElementRecc(root->left);
    Node* rmax = maxElementRecc(root->right);

    if((lmax->data > rmax->data) && (lmax->data > root->data)) {
        return lmax;
    } else if((rmax->data > lmax->data) && (rmax->data > root->data)) {
        return rmax;
    } else {
        return root;
    }
    
}

// We can use any kind of traversal for this
// Time Complexity: O(n) Space Complexity: O(n)
Node* maxElement(Node* root) {

    stack<Node*> s;
    Node* max = new Node(INT_MIN);

    while((root != nullptr) || !s.empty()) {
        while(root != nullptr) {
            s.push(root);
            root = root->left;
        }

        if(s.top()->data > max->data) {
            max = s.top();
        }
        root = s.top()->right;
        s.pop();
    }

    return max;

}

int main() {
    #ifdef ONLINE_JUDGE
        ios::sync_with_stdio(false);
        cin.tie(NULL);
        freopen("input.txt", "r", stdin);
        freopen("output.txt", "w", stdout);
    #endif

    Node a(5);
    Node b(1);
    Node c(12);
    a.left = &b;
    a.right = &c;
    displayNode(maxElementRecc(&a));
    displayNode(maxElement(&a));
    return 0;
}