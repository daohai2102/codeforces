import math
x, y, z = (int(a) for a in raw_input().split())

a = math.sqrt(x*y/z)
b = math.sqrt(x*z/y)
c = math.sqrt(y*z/x)

print 4*int(a) + 4*int(b) + 4*int(c)

