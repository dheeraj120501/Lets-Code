#Demonstration of Logical And having more priority than Logical or
#Refer : Merging Conditions.txt


a = 10
b = 20

#Test 1
#   F  and    F    or     T
if a < 0 and a == b or b > a:
    print('logical and has higher priority as compared to logical or')
else:
    print('logical or has higher priority as compared to logical and')


#Test 2
#   T   or    T    and    F
if a > 0 or a < b  and b == a:
    print('logical and has higher priority as compared to logical or')
else:
    print('logical or has higher priority as compared to logical and')
