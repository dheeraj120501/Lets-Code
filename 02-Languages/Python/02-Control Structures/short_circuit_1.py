#Study of Short circuit behaviour
#Refer : Merging Conditions.txt

def greater(b, c):
    print('Testing: greater')
    return b > c

a = 10
b = 20

print('-----------Test 1--------------')
#Test 1
#    T          and   F
if greater(b,0) and a == 0:
    print('RESULT TRUE')
else:
    print('RESULT: T and F = F')


print('-----------Test 2--------------')
#Test 2
#    F    and   T
if a == 0 and greater(b,0):
    print('RESULT TRUE')
else:
    print('RESULT: F and T = F')


print('-----------Test 3--------------')
#Test 3
#     F           or   T
if greater(b,100) or a > 0 :
    print('RESULT F or T : T')
else:
    print('RESULT FALSE')


print('-----------Test 4--------------')
#Test 4
#    T   or   F
if a > 0 or greater(b,100) :
    print('RESULT: T or F : T')
else:
    print('RESULT FALSE')
