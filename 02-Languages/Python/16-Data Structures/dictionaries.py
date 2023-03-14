# Dictionary: unordered, changeable, indexed
# Contains key-value pairs, key is always immutable item

my_dict = {"name":"Max", "age":28, "city":"New York"}
print(my_dict)

# or use the dict constructor, note: no quotes necessary for keys
my_dict_2 = dict(name="Lisa", age=27, city="Boston")
print(my_dict_2)

# accessing items
name_in_dict = my_dict["name"]
print(name_in_dict)

# NOTE KeyError if no key is found
# print(my_dict["lastname"])

# add a new key
my_dict["email"] = "max@xyz.com"
print(my_dict)

# or overwrite the now existing key
my_dict["email"] = "coolmax@xyz.com"
print(my_dict)

# delete a key-value pair
del my_dict["email"]

# this returns the value and removes the key-value pair
print("popped value:", my_dict.pop("age"))

# return and removes the last inserted key-value pair 
# (in versions before Python 3.7 it removes an arbitrary pair)
print("popped item:", my_dict.popitem())

print(my_dict)

# clear() : remove all pairs
my_dict.clear()

# Searching in dictionary
my_dict = {"name":"Max", "age":28, "city":"New York"}
# use if .. in ..
if "name" in my_dict:
    print(my_dict["name"])

# use try except, to not crash program
try:
    print(my_dict["firstname"])
except KeyError:
    print("No key found") 

# loop over keys
for key in my_dict:
    print(key, my_dict[key])

# loop over keys
print(my_dict.keys())
for key in my_dict.keys():
    print(key)

# loop over values
print(my_dict.values())
for value in my_dict.values():
    print(value)

# loop over keys and values
print(my_dict.items())
for key, value in my_dict.items():
    print(key, value)

dict_org = {"name":"Max", "age":28, "city":"New York"}

# this just copies the reference to the dict, so be careful
dict_copy = dict_org

# now modifying the copy also affects the original
dict_copy["name"] = "Lisa"
print(dict_copy)
print(dict_org)

# use copy(), or dict(x) to actually copy the dict
dict_org = {"name":"Max", "age":28, "city":"New York"}

dict_copy = dict_org.copy()
# dict_copy = dict(dict_org)

# now modifying the copy does not affect the original
dict_copy["name"] = "Lisa"
print(dict_copy)
print(dict_org)

# Use the update() method to merge 2 dicts
# existing keys are overwritten, new keys are added
my_dict = {"name":"Max", "age":28, "email":"max@xyz.com"}
my_dict_2 = dict(name="Lisa", age=27, city="Boston")

my_dict.update(my_dict_2)
print(my_dict)

# use numbers as key, but be careful
my_dict = {3: 9, 6: 36, 9:81}
# do not mistake the keys as indices of a list, e.g my_dict[0] is not possible here
print(my_dict[3], my_dict[6], my_dict[9])

# use a tuple with immutable elements (e.g. number, string)
my_tuple = (8, 7)
my_dict = {my_tuple: 15}

print(my_dict[my_tuple])
print(my_dict[8, 7])

# a list is not possible because it is not immutable
# this will raise an Error:
# my_list = [8, 7]
# my_dict = {my_list: 15}

# Nested dictionary
my_dict_1 = {"name": "Max", "age": 28}
my_dict_2 = {"name": "Alex", "age": 25}
nested_dict = {"dictA": my_dict_1,
               "dictB": my_dict_2}
print(nested_dict)
print(nested_dict["dictB"]["age"]) 

# Unpacking/Destructing dictionary
a,b = my_dict_1
print(b)