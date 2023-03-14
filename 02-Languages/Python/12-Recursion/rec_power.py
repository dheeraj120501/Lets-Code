#Function to cal x raised to y recursively
#refer: recursion.png

def power(no, exp):
    if exp == 0:#base case
        return 1
    else:
        return no * power(no, exp-1)



ans = power(17,4)
print(ans)