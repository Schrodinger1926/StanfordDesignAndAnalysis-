class Heap():

	def __init__(self, array = [None], idx = {} ):
		self.array = array
		self.idx = idx
	
	def insert(self, vertex, key):
		self.array.append([vertex, key])
		self.idx[vertex] = len(self.array) - 1
		self.pushup()

	def delete(self, vertex):
		pos1, pos2 = self.array[vertex][0], self.array[-1][0]
		self.array[vertex], self.array[-1] = self.array[-1], self.array[vertex]
		self.idx[pos1], self.idx[pos2] = self.idx[pos2], self.idx[pos1]
		del self.idx[pos1]
		res = self.array.pop()
		self.pulldown(vertex = vertex)
		return res

	def extractMin(self):
		return self.delete(vertex = 1)

	def pushup(self):
		c = len(self.array) - 1
		while c/2 > 0 and self.array[c][1] < self.array[c/2][1]:
			pos1, pos2 = self.array[c][0], self.array[c/2][0]
			self.array[c], self.array[c/2] = self.array[c/2], self.array[c]
			self.idx[pos1], self.idx[pos2] = self.idx[pos2], self.idx[pos1]
			c = c/2

	def isCondition(self, p):
		res = False
		#1. Check both children
		if 2*p + 1 < len(self.array):
			res = self.array[p][1] > self.array[2*p][1] or self.array[p][1] > self.array[2*p +1][1]
			return res
		#2. Check only the available one
		if 2*p < len(self.array):
			res = self.array[p][1] > self.array[2*p][1]
			return res
		
		return res

	def pulldown(self, vertex):
		p = vertex
		while self.isCondition(p = p):
			# Swap the smaller child with the parent and continue down
			try:
				if self.array[2*p][1] < self.array[2*p+1][1]:
					min_child = 2*p 
				else:
					min_child = 2*p + 1
			except IndexError:
				min_child = 2*p
			
			pos1, pos2 = self.array[p][0], self.array[min_child][0]
			self.array[min_child], self.array[p] = self.array[p], self.array[min_child]
			self.idx[pos1], self.idx[pos2] = self.idx[pos2], self.idx[pos1]
			p = min_child
		
	
	def update(self, vertex, key):
		pos = self.idx[vertex]
		self.delete(vertex = pos)
		self.insert(vertex = vertex, key = key)

	def getHeap(self):
		level = 0
		i = 0
		while i < len(self.array):
			for j in range(2**level):
				i += 1
				if i < len(self.array):
					print self.array[i][1], 
				else:
					break
			
			level += 1
			print ''

	def getValue(self, vertex):
		p = self.idx[vertex]
		return self.array[p][1]


def getMSTPrimsAlgorithm(G, E):
	# #1. Construct heap
	# heap = Heap()
	# for i in range(1, len(G)):
	# 	heap.insert(vertex = i, key = float("inf"))

	#2. response value
	res = 0
	mark = [0 for _ in range(len(G))]
	#. choose starting vertex arbitrarily
	# heap.update(vertex = 1, key = 0)
	# i, k = heap.extractMin()
	mark[] = 1
	for _ in range(len(G)-2):
		# find cheapest edge crossing this cut
		m = float("inf")
		mu = None
		mv = None
		for u,v,e in E:
			if (mark[u] == 0 and mark[v] == 1) or (mark[u] == 1 and mark[v] == 0):
				if e < m:
					m = e
					mu = u
					mv = v
		
		mark[mu], mark[mv] = 1, 1
		res += m
	return res, sum(mark)


def main():
	f = open('pa3.1b.txt', 'rb')
	lines = f.readlines()
	#1. Construct Graph
	V, E  = map(int, lines[0].strip('\n').split(' '))
	G = [[] for _ in range(V+1)]
	E = []
	for line in lines[1:]:
		u, v, e = map(int, line.strip('\n').split(' '))
		# connect both vertices
		G[u].append((v,e))
		G[v].append((u,e)) 
		E.append((u,v,e))
	print getMSTPrimsAlgorithm(G, E)

if __name__ == '__main__':
	main()
