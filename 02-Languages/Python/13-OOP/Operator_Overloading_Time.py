#Operator Overloading
#See Operator Overloading.txt

class Time:
    def __init__(self, a=0, b=0, c=0):
        self.h = a #defining the objects attrribute
        self.m = b #defining the objects attrribute
        self.s = c #defining the objects attrribute

    def display(self):
        print(self.h, self.m, self.s, sep=':')

    #special method to establish support of operator + on Time objects
    def __add__(self, other): # t1+t2 ---> __add__(t1, t2)
        temp = Time()
        temp.h = self.h + other.h
        temp.m = self.m + other.m
        temp.s = self.s + other.s
        return temp


    # special method to establish support of operator > on Time objects
    def __gt__(self, other): #t1 > t2 ---> __gt__(t1, t2)
        if self.h > other.h:
            return True
        elif self.h < other.h:
            return False
        else:
            if self.m > other.m:
                return True
            elif self.m < other.m:
                return False
            else:
                if self.s > other.s:
                    return True
                elif self.s < other.s:
                    return False
                else:
                    return False

    # special method to establish support of operator += on Time objects
    def __iadd__(self, other): #t1+=1 ---> t1=__iadd__(t1, 1)
        temp = Time()
        temp.h = self.h + other
        temp.m = self.m + other
        temp.s = self.s + other
        return temp

def main():
    t1 = Time(1,2,3) #object creation (mem alloc + initialization)
    t2 = Time(10,20)
    
    t1+=10
    t1.display()
    t2.display()

    t3 = t1 + t2 #addition of 2 Time object
    t3.display()

    if t1 > t2:
        print('A')
    else:
        print('B')

main()

