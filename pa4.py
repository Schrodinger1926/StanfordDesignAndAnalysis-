from __future__ import division
import random

def delParallelEdges(adj, u, v):
	#delete all v in adj list of u
	temp = []
	for i in adj[u-1]:
		if i != v:
			temp.append(i)
	adj[u-1] = temp

def randContraction(adj, dyNode):
	for _ in range(200-2):
		
		#2. Select an edge at random
		u = random.choice(dyNode)
		v = random.choice(adj[u-1])

		#3. contract this edge

		# delete self Loops
		delParallelEdges(adj, u, v)
		delParallelEdges(adj, v, u)

		# merge A, B in to A
		adj[u-1].extend(adj[v-1])

		# update adjaceny list
		for i in adj[v-1]:
			for j in range(len(adj[i-1])):
				if adj[i-1][j] == v:
					adj[i-1][j] = u

		# remove v from dyNode
		dyNode.remove(v)

def main():
	
	mini = float("inf")
	for c in range(3*(200*2)):

		#1. Construct graph
		f = open('pa4.txt', 'rb')
		lines = f.readlines()
		adj = []
		for line in lines:
			adj.append([int(i) for i in line.strip('\n').split()][1:])

		#2. Dynamic node list
		dyNode = range(1, 201)
		#3. Run random contraction algorithm
		randContraction(adj = adj, dyNode = dyNode)
		l = len(adj[dyNode[0] - 1])
		if l < mini:
			mini = l

		print (c/(3*(200*2)))*100
		
		f.close()

	print mini

		


if __name__ == '__main__':
	main()
