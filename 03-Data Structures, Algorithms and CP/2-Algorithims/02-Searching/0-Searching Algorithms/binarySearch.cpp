#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

// Reccursive way
int binarySearchRecc(int data, int *a, int s, int e)
{
    if (s > e)
    {
        return -1;
    }

    int mid = s + (e - s) / 2;
    if (data == a[mid])
    {
        return mid;
    }
    else if (data < a[mid])
    {
        return binarySearchRecc(data, a, s, mid - 1);
    }
    else
    {
        return binarySearchRecc(data, a, mid + 1, e);
    }
}

// Iterative way
int binarySearchIter(int data, int *a, int n)
{
    int s = 0, e = n - 1;
    while (s <= e)
    {

        int mid = s + (e - s) / 2;
        if (data == a[mid])
        {
            return mid;
        }
        else if (data < a[mid])
        {
            e = mid - 1;
        }
        else
        {
            s = mid + 1;
        }
    }
    return -1;
}

int main()
{
#ifdef ONLINE_JUDGE
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif

    int a[] = {1, 2, 3, 4, 5, 6, 7, 8, 9};
    cout << binarySearchRecc(7, a, 0, 9)<<endl;
    cout << binarySearchIter(7, a, 9)<<endl;
    return 0;
}