/*
Problem: Optimal Merge Pattern Problem
Given an array A with size n. Assume the array content A[i] indicates the length of the ith file and we want to merge all these files into one single file. Given two files A and B with sizes m and n, the complexity of merging is O(m + n). Find the most optimal way to merge the files such that the complexity of merging is minimum.
*/
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

void printList(vector<int> v) {
    for (int i:v) {
        cout<<i<<" ";
    }
    cout<<endl;
}

int optimalMerge(vector<int> a) {
    vector<int> v;
    while(a.size() != 1) {
        sort(a.begin(), a.end());
        reverse(a.begin(), a.end());
        int temp1 = a[a.size()-1];
        int temp2 = a[a.size()-2];
        a.pop_back();
        a.pop_back();
        a.push_back(temp1+temp2);
        v.push_back(temp1+temp2);
    }
    int p = 0;
    for(int i:v) {
        p += i;
    }
    return p;
}

int main() {
    #ifdef ONLINE_JUDGE
        ios::sync_with_stdio(false);
        cin.tie(NULL);
        freopen("input.txt", "r", stdin);
        freopen("output.txt", "w", stdout);
    #endif

    int n;
    cout<<"Enter the size of the array: ";
    cin>>n;

    vector<int> a;
    for(int i=0; i<n; i++) {
        int temp;
        cout<<"Enter the element: ";
        cin>>temp;
        a.push_back(temp);
    }

    int b = optimalMerge(a);

    cout<<"Optimal complexity is: "<<b<<endl;

    return 0;
}