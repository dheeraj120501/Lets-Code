#Demo of continue statement
#Process numbers 0-9 excluding 5
#See: loop control.png 

for i in range(10): #0-9
    if i == 5:
        continue
    print(i, end=' ')

