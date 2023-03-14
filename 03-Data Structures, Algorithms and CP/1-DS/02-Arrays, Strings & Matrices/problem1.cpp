// You are given an integer N. You need to convert all zeroes of N to 5. 

#include <iostream>
#include <string>
using namespace std;

int main() {
    string s;
    cin>>s;
    for(int i=0; i<s.length(); i++) {
        if(s[i] - '0' == 0)
        s[i] = '5';
    }
    cout<<s;
}