n, m, k = (int(x) for x in raw_input().split())

a = [int(x) for x in raw_input().split()]

count = 0

type1 = 0
type2 = 0

for x in a:
    if x == 1:
        type1 += 1
    else:
        type2 += 1

if type1 < m:
    m -= type1
    k += m
    if k - type2 < 0:
        count = type2 - k
else:
    count = type1 - m
    if k - type2 < 0:
        count += type2 - k

print count
