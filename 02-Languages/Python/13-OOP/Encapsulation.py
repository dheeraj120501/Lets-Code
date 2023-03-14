# Encapsulation
# Encapsulation is the OOP technique to represent an entity.
# A class is defined to group the operation and attributes of the entity.
# Python treats a class as a secondary datatype.

class Clock:
	#A special method of the class
	#It is auto invoked on object creation.
	#It defines and initializes the attributes for the object
	def __init__(self):
		self.h = 0
		self.m = 0
		self.s = 0

	#A method represents a way of doing an operation
	#It requires an object for invokation
	#On call the self reference gets initialized with the memory location of the object
	#The operation done by the method apply on the object, via self.
	def setTime(self, a, b, c):
		self.h = a
		self.m = b
		self.s = c

	#Another method
	def updateTime(self):
		self.s+=1
		if self.s==60:
			self.s = 0
			self.m+=1
			if self.m == 60:
				self.m = 0
				self.h+=1
				if self == 13:
					self.h = 1

	#Another method
	def displayTime(self):
		print(self.h, self.m, self.s, sep=':')

def main():
	#Object is an instance of a class
	#It can store and process data
	#Its storage and processing abilities are defined by the data members and methods of the class
	c = Clock()

	#Object of the class is required to invoke its methods.
	c.setTime(10,11,12)
	c.displayTime()
	c.updateTime()
	c.displayTime()

main()