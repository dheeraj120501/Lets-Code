/*
Problem: Find the nth fibonacci number 
Fibonacci Sequence: 1, 1, 2, 3, 5, 8 ...
Complexity Analysis
- Brute force
  - Time: 2^n
  - Space: n
- Memoization
  - Time: n
  - Space: n
- Tabulation
  - Time: n
  - Space: n
*/

#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

// Using Reccursion
ll RFib(ll n) {
    if(n <= 2) 
    return 1;

    return RFib(n-1)+RFib(n-2);
}

// Using DP (Memoization)
ll MFib(ll n, unordered_map<ll, ll>& m) {
    if(m.find(n) != m.end()) {
        return m.at(n);
    }
        if(n <= 2)
        return 1;

        ll fib = MFib(n-1, m) + MFib(n-2, m);
        pair<ll, ll> p = {n,fib};
        m.insert(p);

        return m.at(n);
}

// Using DP (Tabulation)
int TFib(int n) {

}

int main() {
    #ifdef ONLINE_JUDGE
        ios::sync_with_stdio(false);
        cin.tie(NULL);
        freopen("input.txt", "r", stdin);
        freopen("output.txt", "w", stdout);
    #endif

    cout<< RFib(7) <<endl;
    unordered_map<ll, ll> m;
    cout<< MFib(50, m) <<endl;


    return 0;
}