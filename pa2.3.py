import random


class MinHeap():
	"""docstring for MinHeap"""
	def __init__(self, array = [None]):
		self.array = array

	def insert(self, val):
		self.array.append(val)
		self.pushup()

	def extractMin(self):
		self.array[1], self.array[-1] = self.array[-1], self.array[1]
		res = self.array.pop()
		self.pulldown()
		return res

	def pushup(self):
		c = len(self.array) - 1
		while c/2 > 0 and self.array[c] < self.array[c/2]:
			self.array[c], self.array[c/2] = self.array[c/2], self.array[c]
			c = c/2

	def pulldown(self):
		p = 1
		while self.isCondition(p = p):
			minChildIdx = self.isCondition(p = p)
			self.array[minChildIdx], self.array[p] = self.array[p], self.array[minChildIdx]
			p = minChildIdx

	def isCondition(self, p):
		#1. Check both children
		if 2*p + 1 < len(self.array):
			c = 2*p if self.array[2*p+1] > self.array[2*p] else 2*p+1 
			if self.array[p] > self.array[c]:
				return c
		
		#2. Check only the available one
		if 2*p < len(self.array):
			if self.array[p] > self.array[2*p]:
				return 2*p
		
		return 0

	def getSize(self):
		return len(self.array) - 1

	def getMin(self):
		if self.getSize() > 0:
			return self.array[1]
		return 0


class MaxHeap():
	"""docstring for MinHeap"""
	def __init__(self, array = [None]):
		self.array = array

	def insert(self, val):
		self.array.append(val)
		self.pushup()

	def extractMax(self):
		self.array[1], self.array[-1] = self.array[-1], self.array[1]
		res = self.array.pop()
		self.pulldown()
		return res

	def pushup(self):
		c = len(self.array) - 1
		while c/2 > 0 and self.array[c] > self.array[c/2]:
			self.array[c], self.array[c/2] = self.array[c/2], self.array[c]
			c = c/2

	def pulldown(self):
		p = 1
		while self.isCondition(p = p):
			maxChildIdx = self.isCondition(p = p)
			self.array[maxChildIdx], self.array[p] = self.array[p], self.array[maxChildIdx]
			p = maxChildIdx

	def isCondition(self, p):
		#1. Check both children
		if 2*p + 1 < len(self.array):
			#1. Find bigger child
			c = 2*p if self.array[2*p+1] < self.array[2*p] else 2*p+1 

			#2. compare the winner with parent
			if self.array[p] < self.array[c]:
				return c
		
		#2. Check only the available one
		if 2*p < len(self.array):
			if self.array[p] < self.array[2*p]:
				return 2*p
		
		return 0

	def getSize(self):
		return len(self.array) - 1

	def getMax(self):
		if self.getSize() > 0:
			return self.array[1]
		return 0


def rebalance(minHeap, maxHeap):
	if minHeap.getSize() - maxHeap.getSize() > 1:
		#1. Transfer one element from second half to first half
		maxHeap.insert(minHeap.extractMin())

	if maxHeap.getSize() - minHeap.getSize() > 1:
		#2. Transfer one element from first half to second half
		minHeap.insert(maxHeap.extractMax())


	assert (abs(minHeap.getSize() - maxHeap.getSize()) <= 1), "Tree not balanced"
	return

def getMedian(maxHeap, minHeap):
	if maxHeap.getSize() >= minHeap.getSize():
		return maxHeap.getMax()

	return minHeap.getMin()


def main():
	f = open('pa2.3.txt', 'rb')
	lines = f.readlines()
	res = 0

	#1. initialize heaps
	minHeap = MinHeap()
	maxHeap = MaxHeap()

	#2. Start input stream
	for line in lines:
		x = int(line)
		if x > maxHeap.getMax():
			#1. Insert in second half
			minHeap.insert(x)
		else:
			#2. Insert in first half
			maxHeap.insert(x)

		rebalance(minHeap, maxHeap)

		res += getMedian(maxHeap, minHeap)

	print res%10000


if __name__ == '__main__':
	main()