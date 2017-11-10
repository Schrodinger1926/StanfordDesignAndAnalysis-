import sys
import threading

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
		if len(self.array) > 1 and heapLoc < len(self.array):
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


def allPairDijkstra(G, weights):
	m = float("inf")
	idx = [None, None]
	B = [[]]
	for i in range(1, len(G)):
		A, _B = dijkstra(G, i)
		for j in range(1, len(G)):
			if i != j and A[j] + weights[j] - weights[i] < m:
				m = A[j] + weights[j] - weights[i]
				idx = [i, j]
		B.append(_B)

		sys.stdout.write("\rProgress: %s | ShortestDistance: %s"%((float(i)/len(G))*100, m))
		sys.stdout.flush()

	print ""
	assert (B[idx[0]][idx[0]] == idx[0])
	return idx[0], idx[1], m, B[idx[0]]



def dijkstra(G, s):
	"""
	Returns: Coordinates and value of shortest path s -> all v
	"""
	#0. Mark all unexplored
	mark = [0 for _ in range(len(G))]
	
	#1. Initialize all distances to be infinite
	res = [float("inf") for _ in range(len(G))]

	#2. Initialize last hop for every vertex
	_B = [None for _ in range(len(G))]

	#3. construct heap
	heap = Heap()
	for v in range(1,len(G)):
		heap.insert(vertex = v, key = float("inf"))

	#4. Base case
	heap.update(vertex = s, key = 0)
	i, k = heap.extractMin()
	mark[i], res[i] = 1, k
	_B[i] = i
	

	#5. Start iterating over the edges
	i = s
	for _ in range(len(G)-2):
		for j,w in G[i]:
			if not mark[j] and res[i] + w < heap.getValue(vertex = j):
				heap.update(vertex = j, key = res[i] + w)

		#1. Extract min
		x, k = heap.extractMin()

		#2. cache last hop
		_B[x] = i

		#3. update pointer
		i = x
		mark[i], res[i] = 1, k

	return res, _B

def BellmanFord(G):
	"""
	Returns: new Graph formed after reweighting, new weights, if there is any cycle
	"""
	#1. Current working graoh
	_G = G[:]
	
	#2. New Reweighted Graph
	G_new = [[] for _ in range(len(G))]
	
	#3. connect new vertex s with all other v
	s = 0
	for v in range(1, len(G)):
		_G[s].append([v, 0])

	#4. Reverse graph to fetch incoming edges to vertex
	G_rev = [[] for _ in range(len(G))]
	
	#2. Construct G_rev
	for u in range(len(_G)):
		for v, c in _G[u]:
			G_rev[v].append([u, c])

	#3. Only last round to be remember, space optimization
	A = [float("inf") for _ in range(len(_G))]
	
	#4. Launch base case
	A[0] = 0

	#5. Launch N-1 iterations (N is including s)
	for i in range(len(G)-1):
		current = A[:]
		for v in range(len(G)):
			#1. Global Tounament
			minC = A[v] # A[i-1, v]
			
			#2. local tournament
			for w, c in G_rev[v]: # A[i-1, w] + Cwv
				if c + A[w] < minC:
					minC = c + A[w]
			current[v] = minC
		A = current

		sys.stdout.write("\rBellmanFord Progress: %s"%((float(i)/len(G))*100) + "%")
		sys.stdout.flush()
	
	#5. Check for negative cycle, one extra iteration
	for v in range(len(G)):
		#1. Global Tounament
		minC = A[v] # A[i-1, v]
		
		#2. Check if there is any improvement possible
		for w, c in G_rev[v]: # A[i-1, w] + Cwv
			if c + A[w] < minC:
				#3. negative cycle found, stop immediately
				print "Found negative cycle"
				return G_new, A, True


	#6. Calculate G_new,
	for u in range(1, len(G)):
		for v, w in _G[u]:
			w_new = w + A[u] - A[v]
			assert (w_new >=0),"BF didn't do its job"
			G_new[u].append([v, w_new])

	print ""
	assert (all(i <=0 for i in A)),"BF not correct, some element has distance greater than zero"
	return G_new, A, False


def reconstructShortestPath(B, i, j):
	res = []
	while B[j] != i:
		res.append(j)
		j = B[j]
	res.append(i)
	return res


def cleaner(s):
	return map(int, s.strip('\n').split(' '))


def getGraph(filename):
	'''
	Returns: Graph Adjaceny list, True if all edge length +ve
	'''
	f = open(filename, 'rb')
	lines = f.readlines()
	n, m = cleaner(lines[0])
	#1. Initialize graph
	G = [[] for _ in range(n+1)]
	flag = True
	for line in lines[1:]:
		u, v, c = cleaner(line)
		#1. Add edge
		G[u].append([v,c])
		#2. Negative edge cost check
		flag = flag and c >= 0

	f.close()
	return G, flag


def main():
	Path = {
			 'cost' : float("inf"),
			 'path': []
			}
	
		
	filename = 'pa4.1b.txt'
	G, flag = getGraph(filename)
	
	#1. Check if it has negative cycle using BF
	G_new, weights, cycle = BellmanFord(G)
	if not cycle:
		i, j, cost, B = allPairDijkstra(G_new, weights)
		print cost
		if Path['cost'] > cost:
			#1. reconstruct path and update
			Path['cost'] = cost
			Path['path'] = reconstructShortestPath(B, i, j)
	
	print Path['cost']

if __name__ == '__main__':
	sys.setrecursionlimit(2 ** 20)
	threading.stack_size(2 ** 26)
	thread = threading.Thread(target=main)
	thread.start()
