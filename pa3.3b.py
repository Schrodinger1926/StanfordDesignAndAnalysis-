def clean(s):
	return int(s.strip('\n'))
def main():
	f = open('pa3.3b.txt', 'rb')
	# f = open('test.txt', 'rb')
	lines = f.readlines()
	n = clean(lines[0])
	A = [0, clean(lines[1])]
	for i in range(2,n+1):
		wi = clean(lines[i])
		A.append(max(A[-1], A[-2] + wi))

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