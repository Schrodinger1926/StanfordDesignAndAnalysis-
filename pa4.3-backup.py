import sys
import matplotlib.pyplot as  plt

def cleaner(s):
	return map(float, s.strip('\n').split(' '))

f = open('pa4.3.txt', 'rb')
lines = f.readlines()
N = int(lines[0].strip('\n'))
print N
x, y = [], []
D = {}
for i in range(1, N):
	_ , _x, _y = cleaner(lines[i])
	x.append(_x)
	y.append(_y)
	try:
		D[_y] += 1
	except Exception as e:
		D[_y] = 1

	sys.stdout.write("\rProgress: %s"%((float(i)/N)*100) + "%")
	sys.stdout.flush()

plt.plot(x, y, 'ro')
plt.show()
print ""
keys = D.keys()
print len(keys)
keys = sorted(keys)

diff = [keys[i+1] - keys[i] for i in range(len(keys)-1)]
print min(diff), max(diff), keys[-1] - keys[0]
