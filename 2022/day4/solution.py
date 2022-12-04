import re
ans = 0
ans2 = 0
with open("day4\input.txt") as f:
    input = [tuple(int(c) for c in re.split('-|,', line))
             for line in f.read().splitlines()]

for line in input:
    a, b = set(range(line[0], line[1] + 1)), set(range(line[2], line[3] + 1))
    ans += len(a - b) == 0 or len(b - a) == 0
    ans2 += len(a & b) > 0

print(ans)
print(ans2)
