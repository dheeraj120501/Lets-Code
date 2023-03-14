#Find the GCD of 2 numbers
#Refer: gcd.png and Functions.txt

def gcd(val1, val2):
    # smaller of the two number
    if val1 < val2:
        x = val1
    else:
        x = val2

    #check in range x to 1
    for i in range(x,0,-1): #x to 1 with a step: -1
        if val1 % i == 0 and val2 % i == 0: #and makes i a common factor
            break #stop the process

    return i #GCD

#starts here
n1 = int(input('Enter a number '))
n2 = int(input('Enter a number '))
ans = gcd(n1,n2) #call to gcd with n1 and n2 as parameters
print('GCD: ', ans)
