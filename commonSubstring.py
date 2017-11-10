# x = 'xabcdy'
# y = 'abcdz'
X = 'abcd'
Y = 'xyza'

n = len(X)
m = len(Y)
C = [[0 for _ in range(n+1)] for __ in range(m+1)]
res = -float("inf")
idx = None
for i in range(1, m+1):
	for j in range(1, n+1):
		C[i][j] = C[i-1][j-1] + 1 if X[i-1] == Y[j-1] else 0
		# save max length
		if res < C[i][j]:
			res = C[i][j]
			idx = [i,j]

print res
for i in range(1, m+1):
	print ' '.join(map(str, C[i][1:]))

res = ''
i,j = idx[0], idx[1]
while i > 0 and C[i][j] > 0:
	res += X[i-1]
	i -= 1
	j -= 1

res = res[::-1]
print res
