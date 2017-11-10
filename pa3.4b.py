import sys
from time import time
def clean(s):
	return map(int, s.strip('\n').split(' '))

def main():
	t0 = time()
	f = open('pa3.4b.txt', 'rb')
	lines = f.readlines()
	W, n = clean(lines[0])
	V = [0 for _ in range(W+1)]

	for i in range(1,n+1):
		v, w = clean(lines[i])
		temp = [0 for _ in range(W+1)]
		for j in range(W+1):
			temp[j] = max(V[j], V[j-w] + v) if w <= j else V[j]
		V = temp
		sys.stdout.write("\rProgress: %s"%(100*float(i)/n) + "%")
		sys.stdout.flush()
	print V[W]
	print "Time taken: %s sec"%(time()-t0)


if __name__ == '__main__':
	main()