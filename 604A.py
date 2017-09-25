m = [int(x) for x in raw_input().split()]

w = [int(x) for x in raw_input().split()]

hs, hu = (int(x) for x in raw_input().split())

scores = 0.0
x = 0.0
for i in range(5):
    x += 500.0
    scores += max(0.3*x, (1 - m[i]/250.0)*x - 50.0*w[i])

scores += 100*hs - 50*hu

print int(scores) 
