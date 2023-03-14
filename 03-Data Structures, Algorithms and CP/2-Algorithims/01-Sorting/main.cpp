#include <iostream>

void swapNums(int& a, int& b) {
    int temp = a;
    a = b; 
    b = temp;
}

void printArr(int* a, int n) {
    for(int i=0; i<n; i++){
        std::cout<<a[i]<<" ";
    }
    std::cout<<std::endl;
}

void selectionSort(int* a, int n) {
    for(int i=0; i<n-1; i++) {
        int minIdx = i;
        for(int j=i; j<n; j++) {
            if(a[j] < a[minIdx]) {
                minIdx = j;
            }
        }
        swapNums(a[i], a[minIdx]);
    }
}

void bubbleSort(int* a, int n) {
    for(int i=0; i<n; i++) {
        for(int j=0; j<n-i-1; j++) {
            if(a[j] > a[j+1]) {
                swapNums(a[j], a[j+1]);
            }
        }
    }
}

void modBubbleSort(int* a, int n) {
    bool isSorted = false;
    for(int i=0; i<n; i++) {
        isSorted = true;
        for(int j=0; j<n-i-1; j++) {
            if(a[j] > a[j+1]) {
                swapNums(a[j], a[j+1]);
                isSorted = false;
            }
        }
        if(isSorted) {
            break;
        }
    }
}


void insertionSort(int *a, int n) {
    for(int i=0; i<n; i++) {
        for(int j=i; j>0; j--) {
            if(a[j] < a[j-1]) {
                swapNums(a[j], a[j-1]);
            }else{
                break;
            }
        }
    }
}

int partitionArray(int* a, int pivotIdx, int n) {
    int pivot = a[pivotIdx];
    int i = 0, j = n-1, c = 0;
    while(c <= j) {
        if(a[c] < pivot) {
            swapNums(a[c], a[i]);
            i++;
            c++;
        }else if(a[c] > pivot) {
            swapNums(a[c], a[j]);
            j--;
        }else {
            c++;
        }
    }

    return j;
}

void quickSort(int* a, int n) {
    
    if(n < 2) {
        return;
    }
    
    int d = partitionArray(a, 0, n);
    quickSort(a, d);
    quickSort(a+d+1, n-d-1);

}

int main()
{
    int a[] = {1,5,3,4,9,7};
    int n = sizeof(a)/sizeof(a[0]);
    printArr(a, n);
    insertionSort(a, n);
    printArr(a, n);
    return 0;
}
