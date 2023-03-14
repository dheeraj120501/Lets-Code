#an entity : Complex
class Complex:
    def __init__(self, r, i):
        #auto runs on object creation
        #defines and initializes the object
        #puts the object into initial state
        self.rl = r
        self.im = i

    def display(self):
        print(self.rl, "+i", self.im)

    #this special method will be invoked as: obj1 + obj2
    def __add__(self, other):
        temp = Complex(0,0)
        temp.rl = self.rl + other.rl
        temp.im = self.im + other.im
        return temp

    # this special method will be invoked as: obj1 - obj2
    def __sub__(self, other):
        temp = Complex(0, 0)
        temp.rl = self.rl - other.rl
        temp.im = self.im - other.im
        return temp

    # this special method will be invoked as: obj1 * obj2
    def __mul__(self, other):
        temp = Complex(0,0)
        temp.rl = self.rl * other.rl - self.im * other.im
        temp.im = self.rl * other.im + other.rl * self.im
        return temp

    def __eq__(self, other):
        return self.rl == other.rl and self.im == other.im

    def __ne__(self, other):
        return  not self == other

    def __iadd__(self, other):
        self.rl += other
        self.im += other
        return self

def main():
    c1 = Complex(10,5)
    c2 = Complex(15,3)

    c1.display()
    c2.display()

    #here objects are used as operands of an expression
    c3 = c1 + c2
    c3.display()

    c3 = c1 - c2
    c3.display()

    c3 = c1 * c2
    c3.display()


    if c1 == c2:
        print("c1 and c2 are equal")
    else:
        print("c1 and c2 are not equal")


    c1.display()
    c1+=1
    c1.display()

main()