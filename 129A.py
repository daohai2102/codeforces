n = int(raw_input())

numOfOdd = 0

a = [int(x) for x in raw_input().split()]

for i in a:
    if i%2 != 0:
        numOfOdd += 1

if numOfOdd%2 == 0:
    print n - numOfOdd
else:
    print numOfOdd
