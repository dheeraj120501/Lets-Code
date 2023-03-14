#include <iostream>
#include <vector>

std::vector<std::pair<int,int>> bruteForce(int n);
std::vector<std::pair<int,int>> modifiedWay(int n);

int main() {

    std::cout<<"Enter the number to check\n> ";
    int n;
    std::cin>>n;

    std::cout<<"By Brute force approach\n";
    std::vector<std::pair<int,int>> Bans = bruteForce(n);
    for (auto p: Bans){
        std::cout<<p.first<<" raised to power "<<p.second<<std::endl;
    }
    std::cout<<std::endl;

    std::cout<<"By Modified approach\n";
    std::vector<std::pair<int,int>> Mans = bruteForce(n);
    for (auto p: Mans){
        std::cout<<p.first<<" raised to power "<<p.second<<std::endl;
    }
    std::cout<<std::endl;

    return 0;
}

std::vector<std::pair<int,int>> bruteForce(int n) {
    std::vector<std::pair<int,int>> pFacs;
    if (n == 1) {
        std::pair<int, int> pFac{2, 0};
        pFacs.push_back(pFac);
        return pFacs;
    }
    int d = 2;
    while(n > 1){
        int c = 0;
        while (n%d == 0){
            c++;
            n /= d;
        }
        if(c) {
            std::pair<int, int> pFac{d, c};
            pFacs.push_back(pFac);
        }
        d++;
    }
    return pFacs;
}

std::vector<std::pair<int,int>> modifiedWay(int n) {
    std::vector<std::pair<int,int>> pFacs;
    if (n == 1) {
        std::pair<int, int> pFac{2, 0};
        pFacs.push_back(pFac);
        return pFacs;
    }
    int d = 2;
    while(n > 1 && d*d <= n){
        int c = 0;
        while (n%d == 0){
            c++;
            n /= d;
        }
        if(c) {
            std::pair<int, int> pFac{d, c};
            pFacs.push_back(pFac);
        }
        d++;
    }
    if(n > 1) {
        std::pair<int, int> pFac{n, 1};
        pFacs.push_back(pFac);
    }
    return pFacs;
}