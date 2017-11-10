def clean(s):
	return map(int, s.strip('\n').split(' '))

def main():
	f = open('pa3.4a.txt', 'rb')
	lines = f.readlines()
	W, n = clean(lines[0])
	#1. Intialize 2-D array
	V = [[0 for _ in range(W+1)] for __ in range(n+1)]

	for i in range(1,n+1):
		v, w = clean(lines[i])
		for j in range(W+1):
			V[i][j] = max(V[i-1][j], V[i-1][j-w] + v) if w <= j else V[i-1][j]
	print V[n][W]


if __name__ == '__main__':
	main()