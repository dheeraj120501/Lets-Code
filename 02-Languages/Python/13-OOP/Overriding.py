#Inheritance of Code
#Python allows a sub class to inherit the of code (instance methods) the super class(es).
#Ideally the sub class utilizes the inherited code:
#1) As it is : for processing the super class data.
#2) Overriding it : for applying (run time) polymorphism.

class A:
    #instance methods (code)
    def fx1(self):
        print('A fx1()')

    def fx2(self):
        print('A fx2()')


class B(A): #class B inherits A
    #instance methods (overridden code)
    #Method Overriding is defining an inherited method in the sub class, keeping the methods signature same.
    #By method overriding the sub class provides another way (new body) for doing the same task (same signature).
    #For this the sub class utilizes the extended code and data.
    def fx2(self):
        print('B fx2() starts')
        self.fx3()
        print('B fx2() ends')

    # instance methods (extended code)
    def fx3(self):
        print('B fx3()')

# class C:
#     def fx1(self):
#         print('CCCCCCCCCCCCCCC')
#     def fx2(self):
#         print('DDDDDDDDDDDDDDDDDDDDD')


def polymorphic_behaviour(ref):
    print('----------------------')
    if isinstance(ref, A): #works for A and its sub classes (types), due to compatibliity by inheritance.
        ref.fx1()
        ref.fx2() #polymorphism (multiple definitions (ways) for a task.
    else:
        print('Invalid Type: ', type(ref))
    print('----------------------')

def main():
    polymorphic_behaviour(A())
    polymorphic_behaviour(B())
    polymorphic_behaviour(12)
    #polymorphic_behaviour(C())

main()
