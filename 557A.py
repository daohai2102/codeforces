n = int(raw_input())

min1, max1 = (int(x) for x in raw_input().split())
min2, max2 = (int(x) for x in raw_input().split())
min3, max3 = (int(x) for x in raw_input().split())

def distribute(min1, max1, min2, max2, min3, max3):
	for i in range(min(max1, n - min2 - min3), max(min1 - 1, n - max2 - max3 - 1), -1):
		for j in range(min(max2, n - i - min3), max(min2 - 1, n - i - max3 - 1), -1):
			k = n - i - j
			if k in range(min3, max3 + 1):
				return i, j, k

i, j, k = distribute(min1, max1, min2, max2, min3, max3)

print i, j, k

