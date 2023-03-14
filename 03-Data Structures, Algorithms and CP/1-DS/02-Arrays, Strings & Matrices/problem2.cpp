// Given an array of distinct elements. Find the third largest element in it. 
#include <iostream>
using namespace std;

int main() {
    int n;
    cin>>n;
    int* a = new int[n];
    for(int i=0; i<n; i++)
    cin>>a[i];
    if(n<3) {
        cout<<"-1";
        return 0;
    }
    for(int i=0; i<3; i++) {
        int maxI = i;
        for(int j=i+1; j<n; j++) {
            if(a[maxI]<a[j])
            maxI = j;
        }
        int temp = a[maxI];
        a[maxI] = a[i];
        a[i] = temp;
    }
    
    cout<<a[2];
}