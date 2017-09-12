n = int(raw_input())

a = [int(x) for x in raw_input().split()]

s, t = (int(x) for x in raw_input().split())

sum1 = 0

min1 = min(s, t) - 1
max1 = max(s, t) - 1

for i in range(min1, max1, 1):
	sum1 += a[i]

tmp = min1
min1 = max1
max1 = tmp + n
sum2 = 0
for i in range(min1, max1, 1):
	sum2 += a[i%n]

print min(sum1, sum2)

