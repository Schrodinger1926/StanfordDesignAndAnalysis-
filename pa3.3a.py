import random
import threading
import sys
class MinHeap():
	"""docstring for MinHeap"""
	def __init__(self, array = [None]):
		self.array = array

	def insert(self, node):
		self.array.append(node)
		self.pushup(c = len(self.array) - 1)

	def extractMin(self):
		self.array[1], self.array[-1] = self.array[-1], self.array[1]
		res = self.array.pop()
		if len(self.array) > 1:
			self.pulldown(p = 1)
		return res

	def pushup(self, c):
		while c/2 > 0 and self.array[c].getValue() < self.array[c/2].getValue():
			self.array[c], self.array[c/2] = self.array[c/2], self.array[c]
			c = c/2

	def pulldown(self, p):
		p = p
		while self.isCondition(p = p):
			minChildIdx = self.isCondition(p = p)
			self.array[minChildIdx], self.array[p] = self.array[p], self.array[minChildIdx]
			p = minChildIdx

	def isCondition(self, p):
		#1. Check both children
		if 2*p + 1 < len(self.array):
			c = 2*p if self.array[2*p+1].getValue() > self.array[2*p].getValue() else 2*p+1 
			if self.array[p].getValue() > self.array[c].getValue():
				return c
		
		#2. Check only the available one
		if 2*p < len(self.array):
			if self.array[p].getValue() > self.array[2*p].getValue():
				return 2*p
		
		return 0

	def getSize(self):
		return len(self.array) - 1

	def getMin(self):
		if self.getSize() > 0:
			return self.array[1]
		return 0

	def testHeap(self):
		c = len(self.array) - 1
		while c/2 >= 1 :
			if self.array[c/2].getValue() > self.array[c].getValue():
				return False
			c = c/2
		return True

class Node(object):
	"""docstring for Node"""
	def __init__(self, left = None, right = None, label = None, parent = None, value = None, depth = None):
		self.left = left
		self.right = right
		self.label = label
		self.parent = parent
		self.value = value
		self.depth = depth
	
	def setLeft(self, node):
		self.left = node
	
	def setRight(self, node):
		self.right = node
	
	def setLabel(self, label):
		self.label = label

	def setParent(self, node):
		self.parent = node

	def setValue(self, value):
		self.value = value
	
	def setDepth(self, depth):
		self.depth = depth
	
	def getLeft(self):
		return self.left
	
	def getRight(self):
		return self.right

	def getLabel(self):
		return self.label

	def getParent(self):
		return self.parent

	def getValue(self):
		return self.value

	def getDepth(self):
		return self.depth
		
def getHuffmanCodes(heap):
	#1. Base case
	if len(heap.array) == 3:
		#1. only two elements in heap, merge them
		innerNode = Node(left = heap.array[1], right = heap.array[2], depth = 0)
		for i in range(1,3):
			heap.array[i].setParent(innerNode)
			heap.array[i].setDepth(1)
		return

	#2. Extract two least frequent symbols
	a = heap.extractMin()
	b = heap.extractMin()
	
	#3. Create new symbol ab
	node = Node(value = a.getValue() + b.getValue(), label = a.getLabel() + '*' + b.getLabel())
	heap.insert(node)
	
	#4. Find solution for this smaller alphabet
	getHuffmanCodes(heap)

	#6. Expand symbol ab to a and b
	innerNode = Node(parent = node.getParent(), left = a, right = b, depth = node.getDepth())
	a.setParent(innerNode)
	b.setParent(innerNode)
	a.setDepth(innerNode.getDepth() + 1)
	b.setDepth(innerNode.getDepth() + 1)
	return

def main():
	f = open('pa3.3a.txt', 'rb')
	lines = f.readlines()
	#1. Initialize heap
	heap = MinHeap()
	res = []
	#2. Build heap
	for label, line in enumerate(lines[1:]):
		#1. preprocessing	
		p = int(line.strip('\n'))
		node = Node(value = p, label = str(label))
		res.append(node)
		heap.insert(node)
	
	assert(heap.testHeap())
	#3. get encoding
	getHuffmanCodes(heap)

	d = [node.getDepth() for node in res]
	print min(d), max(d)
if __name__ == '__main__':
	sys.setrecursionlimit(2 ** 20)
	threading.stack_size(2 ** 26)
	thread = threading.Thread(target=main)
	thread.start()
