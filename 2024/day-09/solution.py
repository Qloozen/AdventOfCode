import re
from functools import reduce
from collections import defaultdict

with open("input.txt") as f:
    # lines = [line for line in f.read().splitlines()]
    # 0..111....22222
    # 02.111....2222.
    # 022111....222..
    # 0221112...22...
    # 02211122..2....
    # 022111222......
    t = f.read()

    inital_map = []
    id_index = 0
    for i, num in enumerate(t):

        if i % 2 == 0: 
            inital_map += [str(id_index)] * int(num)
            id_index+=1
        else: inital_map += ['.'] * int(num)
    # print(''.join(inital_map))

    for i in range(len(inital_map)-1, -1, -1):
        first_dot = inital_map.index(".")
        if first_dot > i: break

        inital_map[first_dot] = inital_map[i]
        inital_map[i] = "."


    total = 0
    for i, id in enumerate(inital_map):
        if id == '.': break
        total += i * int(id)
    print(total)