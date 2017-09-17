n = int(raw_input())

num = raw_input().strip()

sum1 = 0
sum2 = 0
check = True

for i in range(n/2):
	tmp = ord(num[i]) - ord('0')
	if not (tmp == 4 or tmp == 7):
		check = False
		break
	sum1 += tmp
if check:
	for i in range(n/2, n):
		tmp = ord(num[i]) - ord('0')
		if not (tmp == 4 or tmp == 7):
			check = False
			break
		sum2 += tmp

if check and sum1 == sum2:
	print "YES"
else:
	print "NO"