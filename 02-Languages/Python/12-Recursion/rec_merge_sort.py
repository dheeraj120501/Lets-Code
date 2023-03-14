#Merge_Sort
def merge_sort(data):
    #split the list into 2 sub lists
    mid = len(data)//2
    sub_data_1 = data[:mid]
    sub_data_2 = data[mid:]

    #sub list 1
    if len(sub_data_1) > 2: #base condition
        merge_sort(sub_data_1)
    elif len(sub_data_1) ==2:
        #sort the sub list by a comparison + swap
        if sub_data_1[0] > sub_data_1[1]:
            temp = sub_data_1[0]
            sub_data_1[0] = sub_data_1[1]
            sub_data_1[1] = temp

    #sub list 2
    if len(sub_data_2) > 2: #base condition
        merge_sort(sub_data_2)
    elif len(sub_data_2) ==2:
        #sort the sub list by a comparison + swap
        if sub_data_2[0] > sub_data_2[1]:
            temp = sub_data_2[0]
            sub_data_2[0] = sub_data_2[1]
            sub_data_2[1] = temp

    #merge
    i= j= k = 0

    while i < len(sub_data_1) and j < len(sub_data_2):
        if sub_data_1[i] <= sub_data_2[j]:
            data[k] = sub_data_1[i]
            i+=1
            k+=1
        else:
            data[k] = sub_data_2[j]
            j+=1
            k+=1

    #copy the rest of the elements of sub_data_1
    while i < len(sub_data_1):
        data[k] = sub_data_1[i]
        i+=1
        k+=1

    #copy the rest of the elements of sub_data_2
    while j < len(sub_data_2):
        data[k] = sub_data_2[j]
        j+=1
        k+=1


def main():
    data = [10,8,5,19, 2,20,15, 6, 11,4,12]
    print(data)
    merge_sort(data)
    print(data)

main()
