from math import floor
from operator import itemgetter

def findMedian(A, left, right):
	# create idx list
	idx = [left, int(floor((left+right)/2)), right]
	t = [(i, A[i]) for i in idx]
	m1 = max(t, key=itemgetter(1))
	t.remove(m1)
	return max(t, key=itemgetter(1))[0]



def setPivot(A, left, right, method):
	if method == "first":
		return
	elif method == "last":
		# swap first and last elememt
		A[left], A[right] = A[right], A[left]
		return
	else:
		#1. find median of 3 elements
		p = findMedian(A = A, left = left, right = right)

		#2. swap with first element
		A[left], A[p] = A[p], A[left]


def partition(A, left, right):
	#1. set partions boundary and unsearched section boundary
	i, j = left, left + 1

	#2. compare all n - 1 elemts with pivot
	while j <= right:
		if A[left] < A[j]:
			pass
		else:
			#3. If smaller, add it into left internal partition
			A[j], A[i+1] = A[i+1], A[j]
			i += 1
		j += 1

	#4. place pivot on partition boundary
	A[left], A[i] = A[i], A[left]
	return i

def quickSort(A, left, right, method = "first"):
	# Base case: 0 or 1 elements, no comparison
	if left >= right:
		return 0
	
	#1. choose a pivot
	setPivot(A = A, left = left, right = right, method = method)

	#2. Partition on this pivot (in-place) and update pivot location
	p = partition(A = A, left = left, right = right)
	
	#3. Recursive compute comparison on left and right partition
	c1 = quickSort(A = A, left = left, right = p-1, method = method)
	c2 = quickSort(A = A, left = p+1, right = right, method = method)

	#4. Number of comparisons in this section
	c3 = right - left

	return c1 + c2 + c3

def main():
	f = open("pa3.txt", "r")
	lines = f.readlines()
	array = [int(line) for line in lines]
	methods = ["first", "last", "median"]
	
	for method in methods:
		A = array[:]
		print quickSort(A = A, left = 0, right = len(A) - 1, method = method)

if __name__ == '__main__':
	main()