/*
 GCD of 2 numbers can be found out using Euclidian Algorithm
*/

#include<bits/stdc++.h>
using namespace std;

int gcd1(int a, int b) {
    if(b == 0) {
        return a;
    }
    return gcd1(b, a%b);
}

int gcd2(int a, int b) {
    while ( b ) {
        a = a % b;
        swap ( a, b );
    }
    return a;
}


int main() {
    cout<<gcd1(40, 64)<<endl;
    cout<<gcd2(40, 64)<<endl;
    cout<<__gcd(40, 64)<<endl;
    return 0;
}