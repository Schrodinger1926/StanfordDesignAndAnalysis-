import sys
import math
import matplotlib.pyplot as plt

from itertools import combinations
from time import time

def cleaner(s):
	return map(float, s.strip('\n').split(' '))


def getSubset(s, V):
	return list(combinations(range(2, V), s))


def getDistance(C, i, j):
	return math.sqrt((C[i][0] - C[j][0])**2 + (C[i][1] - C[j][1])**2)


def getTSPValue(C):
	V = len(C)
	
	#0. Need hashtable to index all the vertex with distance
	D = []

	#1. Initialize array
	A = [float("inf") for _ in range(V)]

	#2. Base cases
	A[1] = 0
	
	#3. Bottom up
	for s in range(2, V):
		current = A[:]

		#1. every subset with size s containing vertex 1, n-1Cs
		ss = getSubset(s-1, V)
		for _ss in ss:
			#2. solve for each vertex j
			_ss = list(_ss)
			_ss.append(1)
			#3. Now shortest distance upto j with _ss vertices, visited once
			for j in _ss:
				if j != 1:
					m = float("inf")
					#4. try connecting each vertex k in _ss other than j with j
					for k in _ss:
						for Htable, d in D[k]:
							_dist = 
						if k != j and A[k] + getDistance(C, k, j) < m:
							m = A[k] + getDistance(C, k, j)
					
					#5. Assign lowest value to j
					current[j] = m
					D[j].append([set(_ss), m])
		current[1] = float("inf")
		A = current
		sys.stdout.write("\rProgress: %s"%((float(s)/(V-1))*100) + "%")
		sys.stdout.flush()
	
	print ""
	#4. Find cheapest way of connecting back to 1
	m = float("inf")
	for d in range(2,V):
		if A[d] + getDistance(C, 1, d) < m:
			m = A[d] + getDistance(C, 1, d)
	return m


def main():
	# f = open('pa4.2.txt', 'rb')
	t0 = time()
	f = open('test.txt', 'rb')
	lines = f.readlines()
	C = [None]
	for line in lines[1:]:
		_x, _y = cleaner(line)
		C.append([_x, _y])
	print getTSPValue(C)
	print "Time taken: %ssec"%(time() - t0)


if __name__ == '__main__':
	main()