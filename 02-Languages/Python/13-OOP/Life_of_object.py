#life of an object
#creation: memory allocation , __init__()
#usage : ref.operations
#deletion: __del__(), memory deallocation

class Person:
    #A special method that is auto invoked as object is created.
    #Initialize the object, put it in first state.
    # Constructor
    def __init__(self, nm):
        self.age = 0
        self.name = nm #define an instance variable, one declaration per object
        print(self.name, ' is born')

    def display(self):
        self.age+=1
        print('Hello ', self.name)

    # A special method that is auto invoked as object is to be removed from memory.
    # Clean the resource and put the object in its last state.
    def __del__(self):
        print(self.name, 'dies')

def fx(ref):
    print('------------in fx------------')
    ref.display() #operation on the object continue
    print('------------fx ends------------')

def main():
    print('In main')
    # life of an object starts
    p = Person('AAA')
    #using the object through the reference
    p.display()
    print('============')
    fx(p)
    print('============')
    p.display()
    print('main ends')

print('~~~~~~~~~~~~~~~~')
main()
print('~~~~~~~~~~~~~~~~')
