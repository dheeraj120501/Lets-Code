#Inheritance of Code
class A:
    #instance methods (code)
    def fx1(self):
        print('A fx1()')

    def fx2(self):
        print('A fx2()')


class B(A): #class B inherits A
    # instance methods (extended code)
    def fx3(self):
        print('B fx3()')

def main():
    objB = B() #object of B
    objB.fx1() #access inherited code (instance methods of A)
    objB.fx2() #access inherited code (instance methods of A)
    objB.fx3() #access extended code (instance methods of B)


main()
