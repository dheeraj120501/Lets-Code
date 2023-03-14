#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int linearSearch(int data, int* a, int n) {
    for(int i=0; i<n; i++) {
        if(a[i] == data) {
            return i;
        }
    }
    return -1;
}

int main() {
    #ifdef ONLINE_JUDGE
        ios::sync_with_stdio(false);
        cin.tie(NULL);
        freopen("input.txt", "r", stdin);
        freopen("output.txt", "w", stdout);
    #endif

    int a[] = {1, 2, 3, 4, 5, 6, 7, 8, 9};
    cout << linearSearch(7, a, 9)<<endl;

    return 0;
}