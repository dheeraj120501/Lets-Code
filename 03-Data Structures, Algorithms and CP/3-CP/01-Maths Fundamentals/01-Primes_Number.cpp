#include <iostream>

bool bruteForce(int n);
bool modifiedWay(int n);

int main() {

    std::cout<<"Enter the number to check\n> ";
    int n;
    std::cin>>n;

    std::cout<<"By Brute force approach: ";
    if(bruteForce(n)) {
        std::cout<<"It is a prime number.\n";
    }else{
        std::cout<<"It is not a prime number.\n";
    }

    std::cout<<"By Modified approach: ";
    if(modifiedWay(n)) {
        std::cout<<"It is a prime number.\n";
    }else{
        std::cout<<"It is not a prime number.\n";
    }

    return 0;
}

bool bruteForce(int n) {
    if(n==0 || n == 1)
    return false;

    for (int i=2; i<=n-1; i++){
        if(n%i == 0)
            return false;
    }
    return true;
}

bool modifiedWay(int n) {
    if(n==0 || n == 1)
    return false;

    for (int i=2; i*i<=n; i++){
        if(n%i == 0)
            return false;
    }
    return true;
}