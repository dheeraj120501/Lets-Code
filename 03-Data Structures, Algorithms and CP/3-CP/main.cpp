#include <bits/stdc++.h>
using namespace std;

vector<int> getTri(int a, int b, int c, int d) {
    vector<int> v(3, -1);

    for(int i=a; i<=b; i++) {
        if(v[0] == -1) {
            v.push_back(i);
            break;
        }
    }

    

}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int t;
    cin>>t;
    while(t--) {
        int a,b,c,d;
        cin>>a>>b>>c>>d;
        vector<int> ans = getTri(a,b,c,d);
        for(int i: ans) {
            cout<<i<<" ";
        }
        cout<<endl;
    }


    return 0;
}