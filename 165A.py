n = int(raw_input())

check = []

for i in range(2001):
	tmp = []
	for j in range(2001):
		tmp.append(False)
	check.append(tmp)
a = []
for i in range(n):
	x, y = (int(x) for x in raw_input().split())
	check[x + 1000][y + 1000] = True
	a.append([x + 1000, y + 1000])

def isSuperCentral(x, y, check):
	top = False
	bottom = False
	left = False
	right = False
	for i in range(x):
		if check[i][y]:
			left = True
			break
	for i in range(x + 1, 2001):
		if check[i][y]:
			right = True
			break
	for i in range(y):
		if check[x][i]:
			bottom = True
			break
	for i in range(y + 1, 2001):
		if check[x][i]:
			top = True
			break
	return top and bottom and left and right

count = 0
for i in a:
	x = i[0]
	y = i[1]
	if isSuperCentral(x, y, check):
		count += 1

print count
