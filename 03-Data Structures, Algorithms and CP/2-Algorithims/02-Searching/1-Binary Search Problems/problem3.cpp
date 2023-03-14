/*
Problem: Find Smallest Letter Greater Than Target
Given a characters array letters that is sorted in non-decreasing order and a character target, return the smallest character in the array that is larger than target.
Note that the letters wrap around so, if target == 'z' and letters == ['a', 'b'], the answer is 'a'.
*/

#include <bits/stdc++.h>
using namespace std;
typedef long long ll;


int ceil (char k, char* a, int n) {
    if(a[n-1] <= k) return 0;
    int s = 0, e = n-1;
    while(s <= e) {
        int mid = s + (e-s)/2;
        if(a[mid] > k) {
            e = mid - 1;
        }else {
            s = mid + 1;
        }
    }
    return s;
}


int main() {
    #ifdef ONLINE_JUDGE
        ios::sync_with_stdio(false);
        cin.tie(NULL);
        freopen("input.txt", "r", stdin);
        freopen("output.txt", "w", stdout);
    #endif

    return 0;
}