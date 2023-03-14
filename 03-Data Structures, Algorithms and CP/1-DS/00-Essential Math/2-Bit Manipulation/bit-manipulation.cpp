// NOTES
/*
Bit manipulation help us do operations faster as they manipulate the bits directly using bit-wise operator i.e. &, |, ~, ^, >>, <<.

NOTE-1: Number of digits in a number n of decimal representation(base 10) is logn + 1 (base of log is 10).
NOTE-2: Number of digits in binary representation(base 2) of a number n of decimal representation(base 10) is logn + 1 (base of log is 2).
NOTE-3: n&(n-1) clear the right most set bit of n.

Properties of XOR
1. a^a = 0
2. a^0 = a

1. To find if a number is odd or even.
2. Swap 2 numbers.
3. Find, Set, Clear and Toggle ith bit.
4. Clearing, Isolating right most set bit.
5. Isolating right most 0 bit. (Isolating a bit mean keeping that bit 1 and rest as zero).
6. Checking Whether Number is Power of 2 or Not.
7. Finding Modulo of a Given Number
8. Reversing the Binary Number
9. Counting Number of One’s in Number
10. Creating Mask for Trailing Zero’s
11. Swap all odd and even bits
12. Performing Average without Division
13. Find number of bits to change in a number a to convert it to b.
*/ 

#include <iostream>

using namespace std;

bool isOdd(int);
void swap(int&, int&);
int getBit(int const &, int);
void setBit(int&, int);
void clearBit(int&, int);
void toggleBit(int&, int);
void clearRight(int&);
void isolateRightSet(int&);
int convertBits1(int const &, int const &);
int convertBits2(int const &, int const &);
int convertBits3(int const &, int const &);

int main() {
    int a = 10;
    int b = 12;
    cout<< a << " " << b << endl;
    swap(a, b);
    cout<< a << " " << b << endl;
    int x = 5;
    cout<<isOdd(x)<<endl;
    cout<<getBit(x, 0)<<endl;
    cout<<getBit(x, 1)<<endl;
    cout<<getBit(x, 2)<<endl;
    setBit(x, 1);
    cout<<x<<endl;
    clearBit(x, 1);
    cout<<x<<endl;
    toggleBit(x, 1);
    cout<<x<<endl;
    clearRight(x);
    cout<<x<<endl;
    isolateRightSet(x);
    cout<<x<<endl;
    cout<<convertBits1(a, b)<<" "<<convertBits2(a, b)<<" "<<convertBits3(a, b)<<endl;
    cout<<convertBits1(x, b)<<" "<<convertBits2(x, b)<<" "<<convertBits3(x, b)<<endl;
    cout<<convertBits1(a, x)<<" "<<convertBits2(a, x)<<" "<<convertBits3(a, x)<<endl;
}

// If a number is odd then it's LSB(right most bit) is 1 else it is 0.
inline bool isOdd(int n) {
    return n&1;
}

// This is achieved by the property of XOR(^) that a^a = 0.
void swap(int& a, int& b) {
    a = a^b;
    b = a^b;
    a = a^b;
}

inline int getBit(int const & n, int pos) {
    return (n & (1<<pos)) > 0;
}

inline void setBit(int& n, int pos) {
    n = n | (1<<pos);
}

inline void clearBit(int& n, int pos) {
    n = n & (~(1<<pos));
}

inline void toggleBit(int& n, int pos){
    n = n ^ (1<<pos);
}

inline void clearRight(int& n){
    n = n & (n-1);
}

inline void isolateRightSet(int& n){
    n = n & (-n);
}

int convertBits1(int const & n1, int const & n2) {
    // M-1 Time complexity is O(number of bits used to store n1)
    int bits = sizeof(n1)*8;
    int xbits = 0;
    for(int i=0; i<bits; i++) {
        if(getBit(n1, i) != getBit(n2, i))
        xbits++;
    }
    return xbits;
}

int convertBits2(int const & n1, int const & n2) {
    // M-2 Reducing the time complexity to O(minimum number of bits in n1^n2)
    int xbits = 0;
    int n = n1^n2;
    while(n) {
        if(n&1 == 1)
        xbits++;
        n = n>>1;
    }
    return xbits;
}

int convertBits3(int const & n1, int const & n2) {
    // M-3 Reducing the time complexity to O(number of set bits in n1^n2)
    int xbits = 0;
    int n = n1^n2;
    while(n) {
        xbits++;
        n = n&(n-1);
    }
    return xbits;
}