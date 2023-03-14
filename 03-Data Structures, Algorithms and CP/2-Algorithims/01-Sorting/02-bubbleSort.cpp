#include <bits/stdc++.h>
using namespace std;

void printArray(int* a, int n) {
    for(int i=0; i<n; i++) {
        cout<<a[i]<<" ";
    }
    cout<<"\n";
}

int main() {
    #ifdef ONLINE_JUDGE
        ios::sync_with_stdio(false);
        cin.tie(NULL);
        freopen("input.txt", "r", stdin);
        freopen("output.txt", "w", stdout);
    #endif

    int n;
    cin>>n;

    int* a = new int[n];
    for(int i=0; i<n; i++) {
        cin>>a[i];
    }

    printArray(a, n);

    for(int i=0; i<n; i++) {
        for(int j=0; j<n-i-1; j++) {
            if(a[j] > a[j+1]) {
                int temp = a[j]; 
                a[j] = a[j+1];
                a[j+1] = temp;
            }
        }
    }

    printArray(a, n);


    return 0;
}