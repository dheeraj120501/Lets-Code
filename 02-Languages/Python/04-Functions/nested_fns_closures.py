# Nested functions and Closures

# A nested function is a function defined inside another function. 
# It is created, used and destroyed dynamically, by the enclosing function, thus hiding it from the global scope.
# It has read only access of variables of the enclosing scope.

# A Closure is a nested function object that remembers values of the enclosing scope even if they are not present in memory. 


def outer_fx(msg):
	print('in outer_fx, msg:', msg)
	msg_len = len(msg)
	#nested function
	def inner_fx():
		#Variables (msg and msg_len) of outer_fx are available for reading only
		#in inner_fx.
		#The names of variables remain the same, but in background they are
		#defined as a read only copy.
		#Such memory objects are termed as closures.
		#Life and scope of closures is controlled by the scope of inner_fx.
		print('in inner_fx, msg:', msg)#closure
		print('length :', msg_len)#closure
		print('inner_fx ends')
	#inner_fx()
	print('outer_fx ends')
	return inner_fx

def main():
	ptr_fx = outer_fx('Python')
	print('---------------')
	ptr_fx()


main()