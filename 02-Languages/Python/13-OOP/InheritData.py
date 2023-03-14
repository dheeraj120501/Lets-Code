#Inheritance of Data
#By inheritance the sub class gets the instance data (object data members) of the super class.
#Further it (sub class) may have self defined instance data members as well.

#TIP: Ensure that the init of sub class invokes the init of super class.

class A:
    def __init__(self):
        print('A init starts')
        self.n1 = 10
        self.n2 = 20
        print('A init ends')

    def display(self):
        print('n1: ', self.n1)
        print('n2: ', self.n2)

class B(A):
    def __init__(self):
        A.__init__(self) #suggested first
        print('B init starts')
        self.ans = self.n1+ self.n2
        print('B init ends')

    def display(self):
        print(self.n1, '+', self.n2, '=', self.ans)


def main():
    objB = B()
    objB.display()

main()