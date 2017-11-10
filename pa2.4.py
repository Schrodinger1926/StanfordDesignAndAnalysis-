from time import time
import sys
import threading

def binarySearchLowerBound(array, left, right, y):
	if left >= right:
		return left

	else:
		#1. Median tending to left
		mid = left + (right - left)/2
		if array[mid] >= y:
			return binarySearchLowerBound(array=array, left=left, right=mid, y=y)
		else:
			return binarySearchLowerBound(array=array, left=mid+1, right=right, y=y)

def binarySearchUpperBound(array, left, right, y):
	if left >= right:
		return left
	
	else:
		#1. Median tending to right
		mid = left + (right - left + 1)/2
		if array[mid] <= y:
			return binarySearchUpperBound(array=array, left=mid, right=right, y=y)
		else:
			return binarySearchUpperBound(array=array, left=left, right= mid-1, y=y)

def main():
	#1. Read data
	to = time()
	f = open('pa2.4.txt', 'rb')
	lines = f.readlines()
	A = []
	for line in lines:
		A.append(int(line))
	
	#2. Sort in-place, why take memory overhead
	A.sort()
	S = set()
	T_low = -10000
	T_high = 10000 
	
	for cnt,x in enumerate(A):
		#1. Find approprate range, which statisfy x + y = t, T_low < t < T_high
		y_low, y_high = T_low - x, T_high - x

		#2. Do binary search on A to find y_low abd y_high
		idx_low = binarySearchLowerBound(array = A, left = 0, right = len(A)-1, y = y_low)
		idx_high = binarySearchUpperBound(array = A, left = idx_low+1, right = len(A)-1, y = y_high) if idx_low < len(A)-1 else idx_low

		#3. count unique t's in this range
		for i in range(idx_low, idx_high+1):
			#1. Double check
			t = x + A[i]
			if t >= T_low and t <= T_high:
				S.add(t)
		cnt = int((float(cnt+1)/len(A))*100)
		sys.stdout.write("\rProgress: %s"%cnt + "%" + "[" + "*"*cnt + " "*(100-cnt) + "]")
		sys.stdout.flush()
	print ''
	print len(S)
	print "Time taken: ", time()-to


if __name__ == '__main__':
	main()
