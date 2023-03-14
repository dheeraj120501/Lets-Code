/*
Problem: Ceil of a number
You are given a sorted array and a number k, find the index of the number greater than or equal to k in the array. If no such element is found return -1.
*/

#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int ceil (int k, int* a, int n) {
    if(a[n-1]<k) return -1;
    int s = 0, e = n-1;
    while(s <= e) {
        int mid = s + (e-s)/2;
        if(a[mid] == k) {
            return mid;
        }else if(a[mid] > k) {
            e = mid - 1;
        }else {
            s = mid + 1;
        }
    }
    return s;
    // Use the below one if don't wanna use the first check
    // return s<n ? s : -1; 
}

int main() {
    #ifdef ONLINE_JUDGE
        ios::sync_with_stdio(false);
        cin.tie(NULL);
        freopen("input.txt", "r", stdin);
        freopen("output.txt", "w", stdout);
    #endif

    int a[] = {2,3,5,9,14,16,18};

    cout<<ceil(-1, a, 7)<<endl; 


    return 0;
}