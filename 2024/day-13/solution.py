import re

with open("input.txt") as f:
    p1 = 0
    p2 = 0

    def solve(coef, const):
        ax, ay, bx, by = coef
        x, y = const

        det_a = (ax * by) - (ay * bx)
        det_x = (x * by) - (y * bx)
        det_y = (y * ax) - (x * ay)

        a_amount = det_x // det_a
        b_amount = det_y // det_a

        return (a_amount, b_amount)


    for line in f.read().split("\n\n"):
        a, b, t = line.split('\n')
        ax, ay = map(int, re.findall(r'\d+', a))
        bx, by = map(int, re.findall(r'\d+', b))
        x, y = map(int, re.findall(r'\d+', t))

        a_amount, b_amount = solve((ax, ay, bx, by), (x, y))

        if a_amount * ax + b_amount * bx == x and a_amount * ay + b_amount * by == y:
            cost = a_amount * 3 + b_amount 
            p1 += cost

        # part 2
        x += 10000000000000
        y += 10000000000000

        a_amount, b_amount = solve((ax, ay, bx, by), (x, y))

        if a_amount * ax + b_amount * bx == x and a_amount * ay + b_amount * by == y:
            cost = a_amount * 3 + b_amount 
            p2 += cost



    print(p1)
    print(p2)