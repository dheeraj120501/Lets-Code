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

    for(int i=0; i<n-1; i++) {
        int min = i;
        for(int j=i+1; j<n; j++) {
            if(a[j] < a[min]) {
                min = j;
            }
        }
        a[i] = a[i]^a[min];
        a[min] = a[i]^a[min];
        a[i] = a[i]^a[min];
    }

    printArray(a, n);

    return 0;
}