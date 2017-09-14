import math
n, m = (int(x) for x in raw_input().split())



tmp = math.sqrt(2.0*m + 0.25) - 0.5

tmp = int(tmp)

while tmp >= n:
	m = m - n*(n + 1)/2
	tmp = math.sqrt(2.0*m + 0.25) - 0.5
	tmp = int(tmp)

print m - tmp*(tmp + 1)/2
