from __future__ import division
import threading
import sys
import math
import gc
from time import sleep
import resource

global Grev, order, stamp, scc


def RevDFS(G, s, mark):
	global stamp, order, Grev
	
	mark[s] = 1
	for j in G[s]:
		if not mark[j]:
			RevDFS(G, j, mark)
		Grev[j].append(s)
	
	order[stamp] = s
	stamp += 1


def DFS(G, s, mark, counter):
	# Check here if we see problem
	# may be just assign a scc value to each vertex
	# if x and -x have same scc value then we are done
	global scc
	mark[s] = 1
	scc[s] = counter
	for j in G[s]:
		if not mark[j]:
			DFS(G, j, mark, counter)
	return


def getIdx(v):
	if v > 0:
		return 2*(v-1) + 1
	return getIdx(abs(v)) + 1


def getNotIdx(v):
	v = -1*v
	return getIdx(v)


def main():
	gc.enable()
	global Grev, order, stamp, scc
	res = [1 for _ in range(7)]
	for ext in range(1,7):
		#1. Construct graph from file
		f = open('pa4.4.'+ str(ext) +'.txt', 'rb')
		# f = open('test.txt', 'rb')
		lines = f.readlines()
		N = int(lines[0])
		G = [[] for _ in range(2*N + 1)]
		for i in range(1, len(lines)):
			line = lines[i]
			u, v = map(int, line.strip('\n').split())
			# connect -u to v
			# connect -v to u
			G[getNotIdx(u)].append(getIdx(v))
			G[getNotIdx(v)].append(getIdx(u))

		f.close()
		print "construction done"
		# Remove parallel edges
		for i in range(1, len(G)):
			s = set(G[i])
			G[i] = list(s)


		# n = 2*N
		stamp = 1
		order = range(len(G))
		Grev = [[] for _ in range(len(G))]
		
		#2. Run reverse dfs and mark finish stamps
		mark = [0 for _ in range(len(G))]
		for node in range(1, len(G)):
			if not mark[node]:
				RevDFS(G, node, mark)
		print "Reverse DFS done"
		#3. Run DFS on Grev and count SCC sizes
		mark = [0 for _ in range(len(G))]
		scc = [None for _ in range(len(G))]
		counter = 0
		for i in range(2*N, 0, -1):
			node = order[i]
			if not mark[node]:
				DFS(Grev, node, mark, counter)
			
			counter += 1
			sys.stdout.write("\rFile %s: %s"%(ext, (float(2*N - i + 1)/(2*N))*100) + "%")
			sys.stdout.flush()
		
		
		#4. Check if x and -x have same scc value
		print ""
		idx = 1
		while idx < len(G):
			if scc[idx] == scc[idx + 1]:
				res[ext] = 0
				break
			idx += 2
		print "Done"
		gc.collect()


	print ''.join(map(str, res[1:]))


if __name__ == '__main__':
	sys.setrecursionlimit(2 ** 20)
	threading.stack_size(2 ** 30)
	thread = threading.Thread(target=main)
	thread.start()
