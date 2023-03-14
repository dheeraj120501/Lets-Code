#Stack using OOP

class Stack:
    def __init__(self):
        self.data = [] #memory container for the Stack
        self.top = -1  #logical representation level upto which the Stack is filled (-1 means empty)

    #Operation to check whether the Stack is empty
    def isEmpty(self):
        return self.top == -1

    #Operation to add a value at top of the Stack(push)
    def push(self, value):
        self.top+=1 #raise the top
        self.data.insert(self.top, value)

    #Operation to remove a value from the top of the Stack(pop)
    def pop(self):
        if not self.isEmpty():
            temp = self.data.pop(self.top)
            self.top-=1 #level (top) falls
            return temp
        else:
            #print('Stack UnderFlow')
            return None

    # Operation to read the value at the top of the Stack(pop)
    def peek(self):
        if not self.isEmpty():
            return self.data[self.top]
        else:
            #print('Stack UnderFlow')
            return None

def dec_to_binary(val):
    s = Stack()
    while val > 0:
        s.push(val %2)
        val = val//2

    bin_val = 0
    while True:
        temp = s.pop()
        if temp != None:
            bin_val = bin_val * 10 + temp
        else:
            break

    return bin_val


def reverse(str_val):
    s = Stack() #object creation (mem allocation + initialization)
    for x in str_val: #say apple
        s.push(x) #a,p,p,l,e
        #push(s,x)

    rev_str_val = ''
    while True:
        temp = s.pop() #e,l,p,p,a
        if temp != None:
            rev_str_val = rev_str_val + temp
        else:
            break

    return rev_str_val

def main():
    q = reverse('apple')
    print(q)

    w = dec_to_binary(1445)
    print(w)

main()