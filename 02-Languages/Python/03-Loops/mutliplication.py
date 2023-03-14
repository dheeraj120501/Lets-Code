#program to generate a multiplcation table
#Refer: loops.png
#See: multiplication.png

n = int(input('Enter a number '))
for i in range(1,11):
    #i varies from 1 to 10
    ans = n * i
    print(n, '*', i, '=', ans)

