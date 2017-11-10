def countInversions(a):
	#1. Base case
	n = len(a)
	if n == 1:
		return a, 0
	
	#2. Recursively break into 2
	A, A_inv = countInversions(a[:n/2])
	B, B_inv = countInversions(a[n/2:])

	#3. Count split inversion
	C, C_inv = countSplitInversions(A, B)

	return C, A_inv + B_inv + C_inv


def countSplitInversions(A, B):
	"""
	A: Sub array sorted
	B: Sub array sorted

	returns sorted A+B, split inversion b/w A and B
	"""

	#1. Add sentinel
	s = float('inf')
	A.append(s)
	B.append(s)
	res = []
	inv = 0
	i, j = 0, 0
	for _ in range(len(A) + len(B) - 2):
		if A[i] < B[j]:
			res.append(A[i])
			i += 1
		else:
			#2. An inversion exists here
			res.append(B[j])
			j += 1
			inv += len(A) - i - 1

	return res, inv


def main():
	#1. Import data into an array
	f = open("pa2.txt", 'r')
	lines = f.readlines()
	a = []
	for line in lines:
		a.append(int(line.strip('\n').strip('\r')))

	_, inversions =  countInversions(a)
	print inversions


if __name__ == '__main__':
	main()