import math
n, m = (int(x) for x in raw_input().split())

def isPrime(x):
	tmp = math.sqrt(x)
	for i in range(2, int(round(tmp)) + 1):
		if x%i == 0:
			return False
	return True

i = n + 1
nextPrime = -1
while True:
	if isPrime(i):
		nextPrime = i
		break
	i += 1

if m == nextPrime:
	print "YES"
else:
	print "NO"