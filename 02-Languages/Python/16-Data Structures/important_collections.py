# Containers
# list, set (unique), dict (key-value), tuple (immutable list), string

# List is a collection which is ordered and mutable. Allows duplicate members.
# Tuple is a collection which is ordered and immutable. Allows duplicate members.
# Set is a collection which is unordered and unindexed. No duplicate members.
# Dictionary is a collection which is unordered, mutable and indexed. No duplicate members.
# Strings are immutable sequences of Unicode code points.

# Collections
# counter, namedTuple(), orderedDict, deafultdict, deque
# - Counter : dict subclass for counting hashable objects 
# - namedtuple() : factory function for creating tuple subclasses with named fields 
# - OrderedDict : dict subclass that remembers the order entries were added, nowdays not used as normal dict also remembers the orders now
# - defaultdict : dict subclass that calls a factory function to supply missing values 
# - deque : list-like container with fast appends and pops on either end

import collections


# Counter:  subclass of dict, key = element, value = count of that element
from collections import Counter

# A counter can take any container as argument
# String is the collection of characters
# Counter will print a dictionary which will have elements as key and their repetation as value, so it's just like a set but it also tells us home many repetation of any element were there in the collection

a = "aaaaabbbbcccdde"
my_counter = Counter(a)
print(my_counter)

print(my_counter.items())
print(my_counter.keys())
print(my_counter.values())

my_list = [0, 1, 0, 1, 2, 1, 1, 3, 2, 3, 2, 4]
my_counter = Counter(my_list)
print(my_counter)

# list of most common items
print(my_counter.most_common(1)) 
print(my_counter.most_common(2)) 

# Return an iterator over elements repeating each as many times as its count. 
# Elements are returned in arbitrary order.
print(list(my_counter.elements()))



from collections import namedtuple
# create a namedtuple with its class name as string and its fields as string
# fields have to be separated by comma or space in the given string
Point = namedtuple('Point','x, y')
pt = Point(1, -4)
print(pt)
print(pt._fields)
print(type(pt))
print(pt.x, pt.y)

Person = namedtuple('Person','name, age')
friend = Person(name='Tom', age=25)
print(friend.name, friend.age)



from collections import OrderedDict
ordinary_dict = {}
ordinary_dict['a'] = 1
ordinary_dict['b'] = 2
ordinary_dict['c'] = 3
ordinary_dict['d'] = 4
ordinary_dict['e'] = 5
# this may be in orbitrary order prior to Python 3.7
print(ordinary_dict)

ordered_dict = OrderedDict()
ordered_dict['a'] = 1
ordered_dict['b'] = 2
ordered_dict['c'] = 3
ordered_dict['d'] = 4
ordered_dict['e'] = 5
print(ordered_dict)
# same functionality as with ordinary dict, but always ordered
for k, v in ordinary_dict.items():
    print(k, v)


# A defaultdict will have a default value if that key has not been set yet.
from collections import defaultdict

# initialize with a default integer value, i.e 0
d = defaultdict(int)  # Intitialises the unkonwn key with int data-type's def value 
d['yellow'] = 1
d['blue'] = 2
print(d.items())
print(d['green'])

# initialize with a default list value, i.e an empty list
d = defaultdict(list)
s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 5)]
for k, v in s:
    d[k].append(v)

print(d.items())
print(d['green'])



# double-ended queue
# Deques support thread safe, memory efficient appends and pops from either side of the deque with approximately the same O(1) performance in either direction.
# The more commonly used stacks and queues are degenerate forms of deques, where the inputs and outputs are restricted to a single end.
from collections import deque
d = deque()

# append() : add elements to the right end 
d.append('a')
d.append('b')
print(d)

# appendleft() : add elements to the left end 
d.appendleft('c')
print(d)

# pop() : return and remove elements from the right
print(d.pop())
print(d)

# popleft() : return and remove elements from the left
print(d.popleft())
print(d)

# clear() : remove all elements
d.clear()
print(d)

d = deque(['a', 'b', 'c', 'd'])

# extend at right or left side
d.extend(['e', 'f', 'g'])
d.extendleft(['h', 'i', 'j']) # note that 'j' is now at the left most position
print(d)

# count(x) : returns the number of found elements
print(d.count('h'))

# rotate 1 positions to the right
d.rotate(1)
print(d)

# rotate 2 positions to the left
d.rotate(-2)
print(d)

# NOTE: An enumerate is a built-in function that provides an index to data structure elements, making iterations through them easier and simpler.
# enumerate() returns an enumerate object.
#     enumerate(iterable, start=0)
#     We generally use them with loops.
#     eg. for i,e in enumerate([1,5,9])
#         i is index and e is element of list if we don't give start index then it will be 0 by default