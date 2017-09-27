stones = raw_input().strip()

insts = raw_input().strip()

pos = 1

for c in insts:
    if c == stones[pos - 1]:
        pos += 1

print pos 
