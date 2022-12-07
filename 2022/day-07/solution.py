ans = 0
ans2 = 0
with open("day-07/input.txt") as f:
    input = f.read().splitlines()

fs = {}
currentDir = []
for line in input:
    parts = line.split()
    if parts[1] == 'cd':
        if parts[2] == '..':
            currentDir.pop()
        else:
            currentDir.append(parts[2]) 
    if parts[0].isnumeric():
        currentDir_copy = currentDir.copy()
        key = '/'.join(currentDir_copy)
        fs[key] = fs.get(key, 0) + int(parts[0])

        for i in range(len(currentDir_copy)):
            currentDir_copy.pop()
            if len(currentDir_copy) < 1:
                continue
            key = '/'.join(currentDir_copy)
            fs[key] = fs.get(key, 0) + int(parts[0])

total_size = fs['/']
available_space = 70000000 - total_size
required_space = 30000000 - available_space

potential = []
for dir, size in fs.items():
    if (size < 100000):
        ans += size
    if size >= required_space:
        potential.append(size)

ans2 = min(potential)

print(ans)
print(ans2)
