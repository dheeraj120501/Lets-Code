#Set operations

def sequential_search(ls, val):
    tot = len(ls)
    for i in range(tot):
        if ls[i] == val:
            return i #index of the matching element
    #never a match
    return -1 #flag

#all elements of set1 and the elements of set2 that are not in set1
def union_set(s1, s2):
    set3 = []
    #set3.extend(s1) #append to set3, all elements of set1
    #or
    for x in s1:
        set3.append(x)

    for x in s2:
        res = sequential_search(s1, x)
        if res == -1: #x not in s1
            set3.append(x)

    return set3

#all common elements of set1 and set2
def intersect_set(s1, s2):
    set3 =[]
    for x in s1:
        res = sequential_search(s2, x)
        if res != -1: #x is common in s1 and s2
            set3.append(x)

    return set3

#Elements of set1 not found in set2
def minus_set(s1, s2):
    set3 = []
    for x in s1:
        res = sequential_search(s2, x)
        if res == -1: #x not found in s2
            set3.append(x)

    return set3

def main():
    set1 = [1,2,3,4,5]
    set2 = [1,3,5,7,9]
    print(set1)
    print(set2)

    set3 = union_set(set1, set2)
    print('Union:', set3)

    set3 = intersect_set(set1, set2)
    print('Intersect:', set3)

    set3 = minus_set(set1, set2)
    print('Set1 Minus Set2:', set3)

main()