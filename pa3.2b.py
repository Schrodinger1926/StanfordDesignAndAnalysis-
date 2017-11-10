import sys
import threading
from time import time

def getHamming(x):
	# HD = 0
	res = [x]
	x = list(x)

	# HD = 1
	for i in range(len(x)):
		# Make separate copy everytime
		temp = x[:]
		temp[i] = '0' if x[i] == '1' else '1'
		temp = ''.join(temp)
		res.append(temp)

	# HD = 2
	for i in range(len(x)-1):
		for j in range(i+1, len(x)):
			temp = x[:]
			temp[i] = '0' if x[i] == '1' else '1'
			temp[j] = '0' if x[j] == '1' else '1'
			temp = ''.join(temp)
			res.append(temp)

	return res


def dfs(G, s, mark):
	mark[s] = 1
	for u in G[s]:
		if not mark[u]:
			dfs(G, u, mark)


def main():
	f = open("pa3.2b.txt",'rb')
	# f = open("test.txt", "rb")
	lines = f.readlines()
	v, b = map(int, lines[0].strip('\n').split(' '))

	#1. construct hash table for O(1) time lookups
	t0 = time()
	D = {}
	for label, vertex in enumerate(lines[1:]):
		x = ''.join(vertex.strip('\n').strip(' ').split(' '))
		try:
			D[x].append(label)
		except Exception as e:
			D[x] = [label]

	#2. construct Graph G
	G = [[] for _ in range(v)]
	for label, vertex in enumerate(lines[1:]):
		
		#1 Generate all vertices with hamming distance at most 2 against x
		x = ''.join(vertex.strip('\n').strip(' ').split(' '))
		validVertices = getHamming(x)
		for u in validVertices:

			#1. check if u actually exist in hash table
			if D.get(u, None) is not None:
				
				#1. Take all the labels in value and connect them with vertex x
				for _label in D[u]:
					
					#1. Avoid self loop
					if _label != label:
						
						#1. Create an undirected edge
						G[label].append(_label)
						G[_label].append(label)

		p = round((float(label)/v)*100, 1)
		sys.stdout.write("\rProgress: %s"%(p) + "%")
		sys.stdout.flush()

	print ""
	#3. Find number of connected components in graph G
	mark = [0 for _ in range(v)]
	res = 0
	for i in range(v):
		if not mark[i]:
			dfs(G, i, mark)
			res += 1
	print res
	print "Time Taken: %ssec"%(round(time() - t0, 2))

if __name__ == '__main__':
	sys.setrecursionlimit(2 ** 20)
	threading.stack_size(2 ** 26)
	thread = threading.Thread(target=main)
	thread.start()
