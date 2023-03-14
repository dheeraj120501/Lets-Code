#Program to reverse a number
#See: loops.png
#Refer: reverse_number.png

#initialization
number = int(input('Enter a number '))#325
reverse = 0
if number >=0:
    print('Number: ', number)
    
    while number >0: #criteria
        #fetch the last digit of the number
        last_digit = number % 10 #5,2,3
        #append the last digit to reverse
        reverse = reverse* 10 + last_digit #5,52,523
        #eliminate the last digit (reintialization)
        number = number // 10 #32,3,0

    print('Reverse:', reverse)
else:
    print('Negative number not allowed')