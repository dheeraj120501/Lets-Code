# Lambda function are anonymous function that has only one expressions
#Ideally a lambda function
#1) represents a mathematical formulae.
#2) is sent as parameter to higher order functions.

add = lambda x,y: x+y
# add is a pointer to the function and is used for invokation
print(add(3,5))

# Custom Sorting
points2D = [(1, 9), (4, 1), (5, -3), (10, 2)]
sorted_by_y = sorted(points2D, key= lambda x: x[1])
print(sorted_by_y)

mylist = [- 1, -4, -2, -3, 1, 2, 3, 4]
sorted_by_abs = sorted(mylist, key= lambda x: abs(x))
print(sorted_by_abs)


# Map function is used to itterate through the itterable and apply the function on every item
l1 = [1, 2, 5, 8]
def mapFunc(i):
    return i**2
print(list(map(mapFunc, l1)))

# Using comprehensions
print([mapFunc(x) for x in l1])

a  = [1, 2, 3, 4, 5, 6]
b = list(map(lambda x: x * 2 , a))

# However, try to prefer list comprehension
# Use map if you have an already defined function
c = [x*2 for x in a]
print(b)
print(c)

# Filter function is used to sort items by certain condition in an itterable, if the condition function return true for that itterable then that item is returned else not
def isEven(i):
    return i%2 == 0
print(list(filter(isEven, l1)))

a = [1, 2, 3, 4, 5, 6, 7, 8]
b = list(filter(lambda x: (x%2 == 0) , a))

# However, the same can be achieved with list comprehension
c = [x for x in a if x%2 == 0]
print(b)
print(c)

# Reduce: reduce(func, seq), repeatedly applies the func to the elements and returns a single value.
# func takes 2 arguments, current element and result of the prev function call.
from functools import reduce
a = [1, 2, 3, 4]
product_a = reduce(lambda x, y: x*y, a)
print(product_a)
sum_a = reduce(lambda x, y: x+y, a)
print(sum_a)