#Sequential Search
#See: sequential_search.png
def sequential_search(ls, val):
    tot = len(ls)
    for i in range(tot):
        if ls[i] == val:
            return i #index of the matching element
    #never a match
    return -1 #flag

def main():
    data = [18,10,33,5,12,16,20,2]
    val = 3
    res = sequential_search(data, val)
    if res == -1:
        print(val, 'not found')
    else:
        print(val, 'found at index', res)

main()