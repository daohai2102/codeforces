n = int(raw_input())

upper_odd = 0
lower_odd = 0
can_be_swaped = False
for i in range(n):
    a, b = (int(x) for x in raw_input().split())
    if (a + b)%2 != 0:
        can_be_swaped = True
    if a%2 != 0:
        upper_odd += 1
    if b%2 != 0:
        lower_odd += 1

if upper_odd%2 == 0 and lower_odd%2 == 0:
    print 0
elif (upper_odd + lower_odd)%2 != 0 or ((upper_odd + lower_odd)%2 == 0 and not can_be_swaped):
    print -1
else:
    print 1
