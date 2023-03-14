#Python memory management
#refer PMM.png
#analyse the output

x = 10
print(x, type(x), id(x))
x+=1
print(x, type(x), id(x))
x+=0.5
print(x, type(x), id(x))
y = x
print(y, type(y), id(y))
x = 100
print(x, type(x), id(x))
print(y, type(y), id(y))