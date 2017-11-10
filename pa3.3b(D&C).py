def clean(s):
	return int(s.strip('\n'))

def getOptimalSet(A):
	#1. recurse on first half
	#2. recurse on second half
	#3. compare if two of them clash, by comparing last and first place occupancy of first half and second half
	#4. if there is a class, you have to compromise in  either one, recurse over the new subset of low weight half


	#1. run 4 recursion possibilities on both the halfs
	#2. A1[-1] = 0 and A2[1] = 0
	#3. A1[-1] = 0 and A2[1] = 1
	#4. A1[-1] = 1 and A2[1] = 0
	
	# forbidden case
	#5. A1[-1] = 1 and A2[1] = 1



def main():
	f = open('test.txt', 'rb')
	# f = open('test.txt', 'rb')
	lines = f.readlines()
	n = clean(lines[0])


	#2. Reconstruction
	S = set()
	i = n
	while i > 0:
		if A[i] == A[i-1]:
			i -= 1
		else:
			S.add(i)
			i -= 2

	assert(A == sorted(A))
	print ''.join(['1' if x in S else '0' for x in [ 1, 2, 3, 4, 17, 117, 517, 997]])


if __name__ == '__main__':
	main()