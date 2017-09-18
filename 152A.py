n, m  = (int(x) for x in raw_input().split())

a = []
check = []
for i in range(n):
    string = raw_input().strip()
    a.append(string)
    check.append(False)

for i in range(m):
    max1 = 0
    tmp = []
    for j in range(n):
        if ord(a[j][i]) > max1:
            max1 = ord(a[j][i])
            tmp = [j]
        elif ord(a[j][i]) == max1:
            tmp.append(j)
    for x in tmp:
        check[x] = True

count = 0
for i in check:
    if i:
        count += 1

print count 

