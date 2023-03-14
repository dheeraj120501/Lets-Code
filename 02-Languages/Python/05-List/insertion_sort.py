#insertion sort
#see: insertion_sort.png
def insertion_sort(data):
    size = len(data) #6
    i = 1 #initial boundary of the sublist
    while i < size: #until the sublist equals the actual list
        current = data[i] #pick
        j = i-1 #left adjacent
        while j >=0: #compare upto the left most element
            if data[j] > current:
                data[j+1] = data[j]
            else:
                break #stop comparison
            j-=1
        #insertion
        data[j+1] = current
        i+=1 #sublist boundary expands

def main():
    data = [5,9,1,4,10,6]
    print(data)
    insertion_sort(data)
    print(data)

main()