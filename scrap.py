# for ext in range(1, 7):
# 	f = open("pa4.4."+ str(ext)+ ".txt", "rb")
# 	lines = f.readlines()
# 	print lines[0]

def getIdx(v):
	if v > 0:
		return 2*(v-1) + 1
	return getIdx(abs(v)) + 1

def getNotIdx(v):
	v = -1*v
	return getIdx(v)


for i in range(1,5):
	print getIdx(i), getNotIdx(i)