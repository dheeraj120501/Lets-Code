# List: ordered, mutable, allows diplicate elements, can be heterogenous

list_1 = ["banana", "cherry", "apple"]
print(list_1)

# Or create an empty list with the list function, an object from list class
list_2 = list()
print(list_2)

# Lists allow different data types (Heterogeneous)
list_3 = [5, True, "apple"]
print(list_3)

# Lists allow duplicates
list_4 = [0, 0, 1, 1]
print(list_4)

item = list_1[0]
print(item)

# You can also use negative indexing, e.g -1 refers to the last item,
# -2 to the second last item, and so on
item = list_1[-1]
print(item)

# Lists can be altered after their creation (Mutable)
list_1[2] = "lemon"
print(list_1)


# Nested Lists
a = [[1, 2], [3, 4]]
print(a)
print(a[0])
print(a[0][1])  # 2D lists


# Iterating over a list by using a for in loop
for i in list_1:
    print(i)

# Searching in lists
if "banana" in list_1:
    print("yes")
else:
    print("no")




my_list = ["banana", "cherry", "apple"]

# len() : get the number of elements in a list
print("Length:", len(my_list))

# append() : adds an element to the end of the list
my_list.append("orange")

# insert() : adds an element at the specified position
my_list.insert(1, "blueberry")
print(my_list)

# pop() : removes and returns the item at the given position, default is the last item
item = my_list.pop()
print("Popped item: ", item)

# remove() : removes an item from the list
my_list.remove("cherry") # Value error if not in the list
print(my_list)

# clear() : removes all items from the list
my_list.clear()
print(my_list)

# reverse() : reverse the items
my_list = ["banana", "cherry", "apple"]
my_list.reverse()
print('Reversed: ', my_list)

# sort() : sort items in ascending order
my_list.sort()
print('Sorted: ', my_list)

# use sorted() to get a new list, and leave the original unaffected.
# sorted() works on any iterable type, not just lists
my_list = ["banana", "cherry", "apple"]
new_list = sorted(my_list)

# create list with repeated elements
list_with_zeros = [0] * 5
print(list_with_zeros)

# concatenation
list_concat = list_with_zeros + my_list
print(list_concat)

# convert string to list
string_to_list = list('Hello')
print(string_to_list)

list_org = ["banana", "cherry", "apple"]

# this just copies the reference to the list, so be careful
list_copy = list_org

# now modifying the copy also affects the original
list_copy.append(True)
print(list_copy)
print(list_org)

# use copy(), or list(x) to actually copy the list
# slicing also works: list_copy = list_org[:]
list_org = ["banana", "cherry", "apple"]

list_copy = list_org.copy()
# list_copy = list(list_org)
# list_copy = list_org[:]

# now modifying the copy does not affect the original
list_copy.append(True)
print(list_copy)
print(list_org)

# a[start:stop:step], default step is 1
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = a[1:3] # Note that the last index is not included
print(b)
b = a[2:] # until the end
print(b)
b = a[:3] # from beginning
print(b)
a[0:3] = [0] # replace sub-parts, you need an iterable here
print(a)
b = a[::2] # start to end with every second item
print(b)
a = a[::-1] # reverse the list with a negative step:
print(a)
b = a[:] # copy a list with slicing
print(b)

# List Comprehension is an elegant and fast way to create a new list from an existing list
a = [1, 2, 3, 4, 5, 6, 7, 8]
b = [i * i for i in a] # squares each element
print(b)

# Destructing/unpacking a list
a,*b,c =[10,12,15,28,77]
print(a)
print(b)
print(c)