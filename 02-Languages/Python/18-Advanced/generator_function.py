#Generator Functions
# Generator functions are functions that generate a series of values.
# An important feature of generator functions is their ability to pass back
# a value to the caller of the function while retaining the state, all through
# the yield statement.
# On next call, it resumes execution from the point next to last yield.

# As a generator function is called first, it returns a Generator object that
# takes care of transfer of yielded values from the function to the point of
# use (iterator loop variable).
# When the generator function ends  StopIteration exception gets raised
# that  destroys the Generator object and stops the iterator loop.


#Example 1:  Generate a fibonacci series of values
#0,1,1,2,3,5,8,13,21,34,55,89,...

def fibonacci(max):
    a = -1
    b = 1
    while True:
        c = a+b #0,1,1,2,3,5,8,...
        if c > max:
            break
        else:
            #print(c, end= ' ') #0,1,1,2,3,5,8,...
            yield c
            a = b #1,0,1,1,2,3,5,...
            b = c #0,1,1,2,3,5,8,...


for x in fibonacci(100):
    print(x, end= ' ')

print()

# Example 2: Generate numbers from min to max
def my_range(min, max):
   x = min # 10
   while x < max:
       yield x
       x+=1

for i in my_range(10, 15):
   print(i)


# Example 3: Generate a multiplication table
def multiplication_table(q):
   for i in range(1,11):
       yield q*i


for res in multiplication_table(18):
   print(res)

