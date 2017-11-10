import random
class Heap(object):
	"""docstring for Heap"""
	def __init__(self):
		self.array = [None]
		self.map = {}

	def insert(self, vertex, key):
		#1. Add in the array end and map location
		self.array.append([vertex, key])
		self.map[vertex] = len(self.array) - 1

		#2. Maintain heap invariant
		self.pushup(heapLoc = len(self.array) - 1)
	
	def extractMin(self):
		assert (len(self.array) > 1), "No elements to extract from"

		#1. Find vertex identities of first and last elements
		pos1, pos2 = self.array[1][0], self.array[-1][0]

		#2. swap both elements
		self.array[1], self.array[-1] = self.array[-1], self.array[1]

		#3. update map
		self.map[pos1], self.map[pos2] = self.map[pos2], self.map[pos1]

		#4. delete last element from array and map
		res = self.array.pop()
		del self.map[pos1]
		
		#5. Maintain invariant
		if len(self.array) > 1:
			self.pulldown(heapLoc = 1)
		return res
	
	def update(self, vertex, key):
		#1. locate vertex in heap
		heapLoc = self.map[vertex]

		#2. Delete element at heap location
		self.delete(heapLoc = heapLoc)

		#3. Re-insert element
		self.insert(vertex = vertex, key = key)


	def delete(self, heapLoc):
		assert (heapLoc < len(self.array)), "index out"

		#1. Find vertex identities of these two locations
		pos1, pos2 = self.array[heapLoc][0], self.array[-1][0]

		#2. swap both elements
		updateElement, lastElement = self.array[heapLoc], self.array[-1]
		self.array[heapLoc], self.array[-1] = self.array[-1], self.array[heapLoc]

		#3. update map
		self.map[pos1], self.map[pos2] = self.map[pos2], self.map[pos1]

		#4. delete last element from array and map
		res = self.array.pop()
		del self.map[pos1]

		#5. Maintain invariant
		if len(self.array) > 1:
			if lastElement[1] > updateElement[1]:
				self.pulldown(heapLoc = heapLoc)
			else:
				self.pushup(heapLoc = heapLoc)


	def pushup(self, heapLoc):
		c = heapLoc
		while c/2 > 0 and self.array[c/2][1] > self.array[c][1]:
			pos1, pos2 = self.array[c/2][0], self.array[c][0]
			self.array[c/2], self.array[c] = self.array[c], self.array[c/2]
			self.map[pos1], self.map[pos2] = self.map[pos2], self.map[pos1]
			c = c/2

	def pulldown(self, heapLoc):
		p = heapLoc
		while self.isChildren(p=p):
			#1. Find min key child
			minChild = float("inf")
			minChildIdx = None

			#2. Find min child
			for i in range(self.isChildren(p=p)):
				if self.array[2*p+i][1] < minChild:
					minChild = self.array[2*p+i][1]
					minChildIdx = 2*p + i
			
			#3. check invariant
			if minChildIdx is not None and self.array[minChildIdx][1] < self.array[p][1]:
				#1. find vertex identities of these two elements
				pos1, pos2 = self.array[minChildIdx][0], self.array[p][0]

				#2. swap elements
				self.array[minChildIdx], self.array[p] = self.array[p], self.array[minChildIdx]

				#3. update map
				self.map[pos1], self.map[pos2] = self.map[pos2], self.map[pos1]

				#4. udpdate parent
				p = minChildIdx

			else:
				break


	def getHeap(self):
		if len(self.array) > 1:
			return self.array[1:]

	def testHeap(self):
		assert (len(self.array) > 1), "No element in heap"
		p = 1
		for p in range(1, len(self.array)):
			#1. Check invariant on child/children
			for i in range(self.isChildren(p=p)):
				if self.array[2*p + i][1] < self.array[p][1]:
					print "Problem at", p, 2*p + i
					return False
		return True 

	def isChildren(self, p):
		if 2*p + 1 < len(self.array):
			return 2
		if 2*p < len(self.array):
			return 1
		return 0

	def getValue(self, vertex):
		heapLoc = self.map[vertex]
		return self.array[heapLoc][1]

def getMSTPrimsAlgorithm(G):
	#1. Construct heap
	heap = Heap()
	for i in range(1, len(G)):
		heap.insert(vertex = i, key = float("inf"))

	#2. response value
	res = 0
	mark = [0 for _ in range(len(G))]
	#. choose starting vertex arbitrarily
	heap.update(vertex = 1, key = 0)
	i, k = heap.extractMin()
	mark[i] = 1
	for v in range(len(G)-2):
		for j, w in G[i]:
			if mark[j] == 0 and heap.getValue(vertex=j) > w:
				heap.update(vertex=j, key=w)
		
		i, k = heap.extractMin()
		mark[i] = 1
		res += k
		assert (heap.testHeap()), "Heap not valid at iteration: %s"%v
	return res, sum(mark)


def heapTest():
	for t in range(1):
		heap = Heap()
		# x =  [[2, 0], [1, 0], [3, 2], [8, 4], [10, 6], [6, 3], [7, 9], [4, 8], [9, 5], [5, 7]]
		x = range(10)
		random.shuffle(x)
		# construct heap
		for i, e in enumerate(x):
			heap.insert(vertex = i+1, key = e)
			assert (heap.testHeap()), "Test failed at build"
		
		res = []
		# lets update each value
		for i, e in enumerate(range(len(x))):
			heap.update(vertex = i+1, key = e)
			print heap.getHeap()
			assert (heap.testHeap()), "Test failed at iteration %s"%(i+1)

	print "Test Passed"
	quit()


def main():
	f = open('pa3.1b.txt', 'rb')
	lines = f.readlines()
	#1. Construct Graph
	V, E  = map(int, lines[0].strip('\n').split(' '))
	G = [[] for _ in range(V+1)]
	for line in lines[1:]:
		u, v, e = map(int, line.strip('\n').split(' '))
		# connect both vertices
		G[u].append((v,e))
		G[v].append((u,e)) 
	print getMSTPrimsAlgorithm(G)

if __name__ == '__main__':
	heapTest()
	main()

