#function to calculate cube of a number and return the result
#Refer: Functions.txt
#See: Python Code.png and Function.png


def cube(num): #on call the num (formal parameter) is initialized with the actual parameter
    sol = num*num*num
    return sol #return (pass back) a value to the caller

print('Function', end = '*')
print('Demo')
x = float(input('Enter a number '))
y = cube(x) #function call with x as parameter (actual)
print('cube of', x, 'is', y)

#FYI:
#input: Takes user keyboard input and makes that available to the program in string form.
#float(string) : Attempt conversion of string into a number. On success the number is returned otherwise ValueError is raised (causing program termination).
