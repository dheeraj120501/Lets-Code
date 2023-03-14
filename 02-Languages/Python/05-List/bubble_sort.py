#bubble sort
#see: bubble_sort.png

def bubble_sort(arr):
    i = len(arr)-1
    while i > 0:
        j = 0
        while j < i:
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
            j+=1
        i-=1


def main():
    lst = [16,20,10,22,7,14]
    print(lst)
    bubble_sort(lst)
    print(lst)

main() #call to main