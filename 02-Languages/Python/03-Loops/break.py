#Demo of break statement
#Generate max 10 numbers or until 50 is generated
#See: loop control.png 

import random #to get the access of predefined functions.

for i in range(1,11): #1-10
    x = random.randint(1,100) #a random int value (whole number) in range 1-100
    print(i, ')', x, )
    if x == 50:
        print("The best number got generated")
        break #stop processing on getting 50