ans = 0
ans2 = 0
with open("day-16/input.txt") as f:
    input = f.read().splitlines()
    nodes = {}
    for line in input:
        name = line.split()[1]
        flow = int(line.split()[4].split('=')[1].split(";")[0])
        children = line.split("valves ")[1].replace(" ", '').split(',')



print(ans)
print(ans2)