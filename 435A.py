n, m = (int(x) for x in raw_input().split())

a = [int(x) for x in raw_input().split()]

count = 0

tmp = 0

for x in a:
    tmp += x
    if tmp > m:
        tmp = x
        count += 1
print count + 1

