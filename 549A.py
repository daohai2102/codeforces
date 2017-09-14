n, m = (int(x) for x in raw_input().split())

image = []

for i in range(n):
	string = raw_input().strip()
	image.append(string)

check = []

f = ord('f') - ord('a')
c = ord('c') - ord('a')
e = ord('e') - ord('a')
a = ord('a') - ord('a')

for i in range(26):
	check.append(False)

count = 0
if n < 2 or m < 2:
	pass
else:
	for i in range(n - 1):
		for j in range(m - 1):
			check[ord(image[i][j]) - ord('a')] = True
			check[ord(image[i + 1][j]) - ord('a')] = True
			check[ord(image[i][j + 1]) - ord('a')] = True
			check[ord(image[i + 1][j + 1]) - ord('a')] = True
			if check[f] and check[a] and check[c] and check[e]:
				count += 1
			check[ord(image[i][j]) - ord('a')] = False
			check[ord(image[i + 1][j]) - ord('a')] = False
			check[ord(image[i][j + 1]) - ord('a')] = False
			check[ord(image[i + 1][j + 1]) - ord('a')] = False

print count