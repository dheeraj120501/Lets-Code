#Study 2: Short Circuit Behaviour
#Refer : Merging Conditions.txt
def LHS_true():
    print('LHS_true')
    return True

def LHS_false():
    print('LHS_false')
    return False

def RHS_true():
    print('RHS_true')
    return True

def RHS_false():
    print('RHS_false')
    return False

# T and F
if LHS_true() and RHS_false():
    print('TRUE')
else:
    print('T and F = F')

print('----------------')


# F and T
if LHS_false() and RHS_true():
    print('TRUE')
else:
    print('F and T = F')

print('----------------')
# F or T
if LHS_false() or RHS_true():
    print('F or T : T')
print('----------------')
# T or F
if LHS_true() or RHS_false():
    print('T or F : T')