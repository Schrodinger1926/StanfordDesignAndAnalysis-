import sys
class Heap():

	def __init__(self, array = [None], idx = {} ):
		self.array = array
		self.idx = idx
	
	def insert(self, vertex, key):
		self.array.append([vertex, key])
		self.idx[vertex] = vertex
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


def dijkstra(G, s):
	#0. Mark all unexplored
	mark = [0 for _ in range(200+1)]
	
	#1. Initialize all distances to be infinite
	res = [1000000 for _ in range(200+1)]

	#3. construct heap
	heap = Heap()
	for v in range(1,201):
		heap.insert(vertex = v, key = 1000000)

	#2. Base case
	heap.update(vertex = s, key = 0)
	i, k = heap.extractMin()
	mark[i], res[i] = 1, k
	

	#3. Start iterating over the edges
	i = s
	for _ in range(200-1):
		for j,w in G[i]:
			if not mark[j] and res[i] + w < heap.getValue(vertex = j):
				heap.update(vertex = j, key = res[i] + w)

		#4. Extract min
		i, k = heap.extractMin()
		mark[i], res[i] = 1, k

	return res



def main():
	n = 200
	G = [[] for _ in range(n+1)]
	#1. Constuct graph
	print "Contructing graph .."
	f = open("pa2.2.txt", 'rb')
	lines = f.readlines()
	for line in lines:
		line = line.strip('\n').strip('\r').split()
		edges = [map(int, e.split(',')) for e in line[1:]]
		# Reduce vertex label by 1]
		G[int(line[0])].extend(edges)

	#2. select start and run dijkstra
	D = dijkstra(G, s = 1)

	#3. preprocess result
	print ','.join(map(str,[D[i] for i in [7,37,59,82,99,115,133,165,188,197]]))

if __name__ == '__main__':
	main()