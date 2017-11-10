X = 'abcdef'
Y = 'afebcd'

n = len(X)
m = len(Y)
C = [[0 for _ in range(n+1)] for __ in range(m+1)]

for i in range(1, m+1):
	for j in range(1, n+1):
		score =  1 if Y[i-1] == X[j-1] else 0
		C[i][j] = max([C[i-1][j], C[i][j-1], C[i-1][j-1] + score])

print C[m][n]
# Reverse it
x, y = '', ''
i,j = m, n
while i > 0 and j >0:
		
		if C[i][j] == C[i][j-1]:
			y += '-'
			x += X[j-1]
			j -= 1
		
		elif C[i][j] == C[i-1][j]:
			y += Y[i-1]
			x += '-'
			i -= 1
		
		

		else:
			y += Y[i-1]
			x += X[j-1]
			i -= 1
			j -= 1

x = x[::-1]
print x
y = y[::-1]
print y