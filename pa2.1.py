from __future__ import division
import threading
import sys
import math

n = 875714
stamp = 0
order = range(n)
Grev = [[] for _ in range(n)]


def RevDFS(G, s, mark):
	global stamp, order, Grev
	
	mark[s] = 1
	for j in G[s]:
		if not mark[j]:
			RevDFS(G, j, mark)
		Grev[j].append(s)
	
	order[stamp] = s
	stamp += 1


def DFS(G, s, mark, counter = 0):
	mark[s] = 1
	for j in G[s]:
		if not mark[j]:
			counter = DFS(G, j, mark, counter)
	counter += 1
	return counter


def main():
	G = [[] for _ in range(n)]
	
	#1. Construct graph from file
	print "Reading file ..."
	f = open('pa2.1.txt', 'rb')
	lines = f.readlines()
	print "Graph contruction begins .."
	count = 0
	for line in lines:
		u, v = map(int, line.strip('\n').split())
		G[u-1].append(v-1)
		count += 1
	print "Completed. Total edges: %s"%count

	#2. Run reverse dfs and mark finish stamps
	mark = [0 for _ in range(n)]
	for node in range(n):
		if not mark[node]:
			RevDFS(G, node, mark)
	print "ordering, Grev done"
	#3. Run DFS on Grev and count SCC sizes
	print "scc computation begins .. "
	scc = []
	mark = [0 for _ in range(n)]
	for i in range(n-1, -1, -1):
		node = order[i]
		if not mark[node]:
			size = DFS(Grev, node, mark)
			scc.append(size)
		sys.stdout.write("\rProgress: %s"%math.floor(((n - i)/n)*100))
		sys.stdout.flush()
	
	print ''
	print "%s scc's computed"%len(scc)
	
	#4. return top 5
	scc.sort(reverse=True)
	print "Top Five"
	d = 5 - len(scc)
	if d > 0:
		scc.extend([0]*d)

	print ','.join(map(str, scc[:5]))


if __name__ == '__main__':
	sys.setrecursionlimit(2 ** 20)
	threading.stack_size(2 ** 26)
	thread = threading.Thread(target=main)
	thread.start()


