#constructor for complex numbers

def complex(a,b):
	return [a,b]

def real(x):
	return x[0]
def imaginary(x):
	return x[1]

#methods for complex numbers
def print_complex(x):
	print(real(x) + " " + "i"*imaginary(x))

def add_complex(x,y):
	a1 = x[0]
	a2 = y[1]
	b1 = x[1]
	b2 = y[1]
	return complex(a1 + a2,b1 + b2)

def sub_complex(x,y):
	a1 = x[0]
	a2 = y[1]
	b1 = x[1]
	b2 = y[1]

	return complex(a1 - a2, b1 - b2)

def mod(x):
	md = -x[1]
	return complex(x[0], md)

def multiply_complex(x,y):
	a1 = x[0]
	a2 = y[1]
	b1 = x[1]
	b2 = y[1]

	a = a1 * a2 - b1*b2 
	b = a1 * b2 + a2*b1

	return complex(a,b)





