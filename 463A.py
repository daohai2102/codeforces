n,s = (int(x) for x in raw_input().split())

change = -1

for i in range(n):
	x, y = (int(x) for x in raw_input().split())
	if x < s:
		if y != 0 and change < 100 - y:
			change = 100 - y
		elif y == 0 and y > change:
			change = 0
	elif x == s and y == 0 and change == -1:
		change = 0
print change