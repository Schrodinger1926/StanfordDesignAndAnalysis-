import sys
import math

class Node(object):
	"""docstring for node"""
	def __init__(self, nxt = None, prev = None, location = None, ID = None):
		self.nxt = nxt
		self.prev = prev
		self.location = location
		self.ID = ID


def cleaner(s):
	return map(float, s.strip('\n').split(' '))

def sqrDist(x, y):
	return (x.location[0] - y.location[0])**2 + (x.location[1] - y.location[1])**2

def main():
	f = open("pa4.3.txt", "rb")
	lines = f.readlines()
	N = int(lines[0])
	C = []
	#1. Initialize nodes
	for i in range(1, N+1):
		ID, _x, _y = cleaner(lines[i])
		C.append(Node(location = [_x, _y], ID = ID))

	#2. Make linked list
	for i in range(1, len(C)-1):
		C[i].nxt = C[i+1]
		C[i].prev = C[i-1]
	
	C[0].nxt = C[1]
	C[-1].prev = C[-2]

	d = 0
	path = []
	#3. Launch city search
	C[1].prev = None
	listHead = C[1]
	s = C[0]
	path.append(s.ID)
	for i in range(len(C)-1):
		#1. Find nearest point to s
		m = float("inf")
		node = None
		head = listHead
		assert(head is not None), "Nothing available in list"
		while head:	
			_d = sqrDist(head, s)
			if _d < m:
				node = head
				m = _d
			
			head = head.nxt

		assert(node is not None), "Couldn't find nearst city"
		#2. delete nearest node from linked list
		if node.prev and node.nxt:
			node.prev.nxt = node.nxt
			node.nxt.prev = node.prev

		elif node.prev is None and node.nxt is None:
			pass

		elif node.prev is None:
			node.nxt.prev = node.prev
			#1. Also update head of linked list
			listHead = node.nxt

		else:
			node.prev.nxt = node.nxt

		#3. Update last city
		s = node

		#4. Increment path length
		d += math.sqrt(m)

		path.append(s.ID)

		sys.stdout.write("\rProgress: %s"%((float(i+2)/N)*100) + "%")
		sys.stdout.flush()
		# print path, d

	#4. Return to first city
	d += math.sqrt(sqrDist(C[0], s))
	path.append(C[0].ID)
	print ""
	print d

if __name__ == '__main__':
	main()




		