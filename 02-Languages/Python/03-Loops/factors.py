#program to find the factors of  a number
#Refer: loops.png
#See: factors.png

n = int(input('enter a number '))
print('factors of ', n, ':')
for i in range(1,n+1):
    #i varies from 1 to n
    if n % i == 0:
        print(i, end= ' ')
