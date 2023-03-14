#class members
#Python allows definition of class level data members and methods.
#They dont act on the object, rather they do some class level processing.
#They are accessible through the class reference.

class Cryptography:
    #Data member that are defined in the class are class level data.
    #They are defined once for the class, not for an object.
    #They are accessible using the class reference (Example: Cryptography.map)
    #They are defined on first use of the class and have a life equal to the life of the application.
    map = {}    #This is class variable as this is declared in class.

    #Methods that act on class data are class methods.
    #They dont require object for ivokation, rather they are called using class reference.
    #They dont act on the state of the object.
    @classmethod
    def setMap(cls):
        k= [chr(x) for x in range(65, 91)]
        v= [chr(y) for y in range(122, 96, -1)]
        for key,val in zip(k,v):
            cls.map[key] = val

        k = [chr(x) for x in range(97, 123)]
        v = [chr(y) for y in range(90, 64, -1)]
        for key, val in zip(k, v):
            cls.map[key] = val

        print(cls.map)

    def __init__(self, data):
        if len(Cryptography.map) == 0:
            Cryptography.setMap()

        self.data = data

    def display(self):
        print(self.data)

    def encrypt(self):
        temp = ''
        for x in self.data: #'Vikas'
            if x in Cryptography.map:
                temp = temp + Cryptography.map[x]
            else:
                temp = temp + x

        self.data = temp


    def decrypt(self):
        temp = ''
        for x in self.data:  # 'Vikas'
            if x in Cryptography.map:
                temp = temp + Cryptography.map[x]
            else:
                temp = temp + x

        self.data = temp


def main():
    objects  = [Cryptography('This is a sample sentence'), Cryptography('OOP is intresting')]

    for o in objects:
        o.display()

    for o in objects:
        o.encrypt()

    for o in objects:
        o.display()

    for o in objects:
        o.decrypt()

    for o in objects:
        o.display()


main()
