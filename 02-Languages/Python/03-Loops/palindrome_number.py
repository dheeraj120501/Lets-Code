#Program to check whether a given number is a palindrome number or not.
#Examples of palindrome numbers: 505, 2222, 3883, 131
#See: loops.png
#Refer: reverse_number.py

#initialization
number = int(input('Enter a number '))#505
reverse = 0

if number >=0:
    backup = number #505

    while number >0: #criteria
        #fetch the last digit of the number
        last_digit = number % 10 #5,0,5
        #append the last digit to reverse
        reverse = reverse* 10 + last_digit #5,50,505
        #eleminate the last digit (reintialization)
        number = number // 10 #50,5,0

    number = backup #restore 505

    if number == reverse:
        print(number , 'is a palindrome number')
    else:
        print(number, 'is not a palindrome number')

else:
    print('Negative number not allowed')