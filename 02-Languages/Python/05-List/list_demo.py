#Demonstration of list
#Refer: list.png

#lst = [] # empty list
#lst = ['sunday', 10, 9.5, True] #list with heterogenous values preset
lst = [10, 8, 30, 5, 9, 10, 15, 40] #list with preset values
print(lst)

#sort
lst.sort(reverse=True)
print(lst)

#search (membership operator in)
if 11 in lst:
    print('list has 11')
else:
    print('11 not in list')
    print('lets add 11')
    lst.append(11) #add the element at the end of the list
    lst.sort(reverse=True)
print(lst)

#find the number of occurrences of 10 in list
print('10 occurs ', lst.count(10), 'times in ', lst)

#reverse the list
lst.reverse()
print(lst)

#iterate over the list
for x in lst:
    if x == 10:
        x = 100 #doesnt update the list
    print(x, end=' ')
print()
print(lst)

#index based traversal
i =0
while i < len(lst):
    if lst[i] == 10:
        lst[i] = 100 #updates the list
    print(lst[i], end = ' ')
    i+=1
print()
print(lst)