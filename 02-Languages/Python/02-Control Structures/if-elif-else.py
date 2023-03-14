#Demonstration of if-elif-else statements
#Refer: Conditional Branching.txt
#See: if-elif-else.png

print("Conditional Branching Test Begins") #message
a = -10 #variable named a will get declared and assigned a value : -10
if a > 0: #criteria
    print(a, "is a positive number")
elif a < 0 : #criteria
    print(a, "is a negative number")
else:
    print(a , "is zero")

print("Conditional Branching Test Ends")

#FYI:
# > is a comparison operator. It compares the LHS value being greater than RHS value and returns a boolean.
# < is a comparison operator. It compares the LHS value being less than RHS value and returns a boolean.
