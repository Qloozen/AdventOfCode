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
    last_id = 0
    for i, num in enumerate(t):

        if i % 2 == 0: 
            inital_map.append((str(last_id), num))
            if i < len(t) - 2:
                last_id+=1
        else: 
            if num != '0':
                inital_map.append((".", num))

    while last_id != 0:
        target_index, target = [(i, x) for i, x in enumerate(inital_map) if x[0] == str(last_id)][0]
        target_el, target_amount = target

        for i in range(len(inital_map)):
            el, space = inital_map[i]
            if i > target_index: break
            if el == "." :
                if target_amount == space: 
                    inital_map[target_index] = (".", target_amount)
                    inital_map[i] = target
                    break
                elif int(target_amount) < int(space):
                    left_over = int(space) - int(target_amount)
                    
                    inital_map[i] = (".", str(left_over))
                    inital_map[target_index] = (".", target_amount)
                    inital_map.insert(i, target)
                    break
        last_id -= 1
                
    t = 0
    
total = 0
pos = 0
for el, amount in inital_map:
    for _ in range(int(amount)):
        if el != ".":
            total += int(el) * pos
        pos += 1
print(total)
