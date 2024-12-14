import re

with open("input.txt") as f:

    def find_lowest(a, b, target):
        options = []

        for i in range(target // a + 1):
            remaining = target - i * a
            for j in range(remaining // b + 1):
                total = i * a + j * b
                if target == total: 
                    cost = 3 * i + 1 * j
                    options.append((i, j, cost))

        return sorted(options, key=lambda x: x[2])

    p1 = 0
    for line in f.read().split("\n\n"):
        a, b, t = line.split('\n')
        ax, ay = map(int, re.findall(r'\d+', a))
        bx, by = map(int, re.findall(r'\d+', b))
        x, y = map(int, re.findall(r'\d+', t))


        lowest_x = find_lowest(ax, bx, x)
        for num_a, num_b, cost in lowest_x:
            t = num_a * ay + num_b * by 
            if num_a * ay + num_b * by == y:
                p1 += cost
    print(p1)