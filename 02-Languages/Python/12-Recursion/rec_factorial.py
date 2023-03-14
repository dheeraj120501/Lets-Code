#Write a recursive solution for finding factorial of a number
#Factorial of:
#5! =  5*4*3*2*1
#4! =  4*3*2*1
#5! =  5*4!
#In general terms
#n! =  n*(n-1)!
#Base case:
#0! = 1


def factorial(n):
    if n == 0: #base case
        return 1
    return n* factorial(n-1)

def main():
    x = 5
    if x >= 0:
        ans = factorial(x)
        print(x, '! = ', ans)
    else:
        print('Factorial of ', x, ' doesnt exist')

main()