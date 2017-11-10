# -*- coding: utf-8 -*-
from __future__ import division 

def getWeightedSum(A):
	c = 0
	res = 0
	for w,l,d in A:
		c += l
		res += w*c
	return res

def main():
	f = open('pa3.1a.txt', 'rb')
	lines = f.readlines()
	A = []
	B = []
	#1. Construct data
	for line in lines[1:]:
		w, l = map(int, line.strip('\n').split(' '))
		A.append((w, l, w-l))
		B.append((w, l, w/l))

	#2. Sort by W (high->low)
	A = sorted(A, key=lambda x:x[0], reverse=True)

	#3. Sort by difference (high->low), ratio (high->low)
	A = sorted(A, key=lambda x:x[2], reverse=True)
	B = sorted(B, key=lambda x:x[2], reverse=True)

	#4. get weigted sums
	print getWeightedSum(A)
	print getWeightedSum(B)

if __name__ == '__main__':
	main()