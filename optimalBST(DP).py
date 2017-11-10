# F = [5, 40, 8, 4, 10, 10, 23]
F = [0.2, 0.05, 0.17, 0.1, 0.2, 0.03, 0.25]
#1 Initialize matrix
C = [[0 for _ in range(len(F))] for __ in range(len(F))]

# Vary window size on array and keep finding optimal value
for s in range(0, len(F)):
	for i in range(len(F)):
		m = float("inf")
		for r in range(i, i+s+1):
			C1 = C[i][r-1] if i <= r-1 <= len(F)-1  else 0
			C2 = C[r+1][i+s] if r+1 <= i+s <= len(F)-1 else 0
			m = C1 + C2 if C1 + C2 < m else m
		
		if i+s < len(F):
			C[i][i+s] = sum(F[i:i+s+1]) + m

print C[0][6]
