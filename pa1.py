from math import ceil, floor
def karatsuba(x, y):
	#1. check if x and y are single digit
	_x, _y = str(x), str(y)
	if x < 10 or y < 10:
		return x*y

	
	#2. make equal lengths
	if len(_x) < len(_y):
		_x = abs(len(_x) - len(_y))*'0' + _x
	else:
		_y = abs(len(_x) - len(_y))*'0'+ _y

	n = len(_x)
	s = int(floor(float(n)/2))
	m = int(ceil(float(n)/2))
	
	#3. Break x and y into subparts
	a, b = _x[:s], _x[s:]
	c, d = _y[:s], _y[s:]

	ac = recurse(int(a), int(c))
	bd = recurse(int(b), int(d))

	ad_bc = recurse(int(a) + int(b), int(c) + int(d)) - ac - bd

	return int((10**(2*m))*ac + (10**(m))*ad_bc + bd)


print karatsuba(3141592653589793238462643383279502884197169399375105820974944592,2718281828459045235360287471352662497757247093699959574966967627)