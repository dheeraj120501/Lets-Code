#Find the minimum value in the list
#refer: list.png
#see: list_minimum.png
def minimum(lst):
    min = 0 #assumption for being smallest
    #compare in range (min+1 to the last element of list)
    i =min+1 #adjacent to the assumed smallest
    upperlimit = len(lst)
    while i < upperlimit:
        if lst[i] < lst[min]:
            min = i #update the minimum
        i+=1

    return min #index of smallest element

lst = [10,7,15,5,22,12]
print(lst)
pos = minimum(lst)
print('Smallest value in list ', lst[pos], 'is at index', pos)