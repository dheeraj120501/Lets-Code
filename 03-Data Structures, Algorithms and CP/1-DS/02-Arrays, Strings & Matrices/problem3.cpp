// Given an array arr[] of size N of positive integers which may have duplicates. The task is to find the maximum and second maximum from the array, and both of them should be distinct, so If no second max exists, then the second max will be -1.

#include<iostream>
using namespace std;

int main() {
    int n;
    cin>>n;
    int* a = new int[n];
    for(int i=0; i<n; i++) {
        cin>>a[i];
    }
    int maxI = 0;
    for(int i=1; i<n; i++) {
        if(a[i] > a[maxI]) {
            maxI = i;
        }
    }
    int temp = a[maxI];
    a[maxI] = a[0];
    a[0] = temp;
    maxI = 1;
    for(int i=2; i<n; i++) {
        if(a[i] > a[maxI] && a[i] < a[0]) 
        maxI = i;
    }
    if(a[maxI] < a[0])
    cout<<a[0]<<" "<<a[maxI];
    else
    cout<<a[0]<<" "<<"-1";
}