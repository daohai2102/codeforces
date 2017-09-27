n = int(raw_input())

a = [int(x) for x in raw_input().split()]

def gcd(a, b):
    if a%b == 0:
        return b
    else:
        return gcd(b, a%b)

def gcd_array(a):
    tmp = gcd(a[0], a[1])
    for i in range(2, n):
        tmp = gcd(tmp, a[i])
    return tmp

print gcd_array(a)*n

