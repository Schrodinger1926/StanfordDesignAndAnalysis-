def update(sL, bL, G, leaderList):
	leaderList[sL] = bL
	for u in G[sL]:
		if leaderList[u] != bL:
			update(u, bL, G, leaderList)


def Find(u, L):
	return L[u]


def Union(sL, bL, leaderList, sizeList, G):
	#1. Update all leader pointer of connected components of small cluster
	update(sL, bL, G, leaderList)

	#2. Update size of new cluster
	sizeList[bL] += sizeList[sL]


def main():
	f = open('pa3.2a.txt', 'rb')
	lines = f.readlines()
	V = int(lines[0].strip('\n'))
	E = []
	for line in lines[1:]:
		u, v, e = map(int, line.strip('\n').split(' '))
		E.append((u,v,e))

	#2. Sort edges according to edge cost (low -> high)
	E = sorted(E, key=lambda x:x[2])

	#3. Intialize Graph, Size list and leader list
	G = [[] for _ in range(V+1)]
	S = [1 for _ in range(V+1)]
	L = [i for i in range(V+1)]

	#4. Iterate over edges
	k = V
	for i,(u,v,e) in enumerate(E):
		#1. If u,v in separate clusters
		if k >= 4:
			if Find(u, L) != Find(v, L):
				#1. Update leader pointers of smaller cluster and size of new leader
				if S[Find(u, L)] < S[Find(v, L)]:
					Union(sL=Find(u, L), bL=Find(v, L), leaderList=L, sizeList=S, G=G)
				else:
					Union(sL=Find(v, L), bL=Find(u, L), leaderList=L, sizeList=S, G=G)

				#2. Connect u, v in G
				G[u].append(v)
				G[v].append(u)

				k -= 1
		
		else:
			print E[i-1][2]
			return


if __name__ == '__main__':
	main()