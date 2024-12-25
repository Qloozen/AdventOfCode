import re
from functools import reduce
from collections import defaultdict, Counter, deque

with open("input.txt") as f:
    s1, s2 = f.read().split('\n\n')

    storage = {}
    for line in s1.splitlines():
        wire, val = line.split(': ')
        storage[wire] = int(val)

    instructions = []
    for inst in s2.splitlines():
        parts = inst.split()
        op = 0
        instructions.append((parts[0], parts[1], parts[2], parts[4])) # in1, op, in2, out
    
    
    q = deque(instructions)
    while q:
        inst = q.popleft()
        in1, op, in2, out = inst

        keys = storage.keys()
        if in1 not in storage or in2 not in storage:
            q.append(inst)
            continue
        
        res = None
        a = storage[in1]
        b = storage[in2]
        if op == 'AND': res = storage[in1] & storage[in2]
        elif op == 'OR': res = storage[in1] | storage[in2]
        elif op == 'XOR': res = storage[in1] ^ storage[in2]

        assert res is not None

        storage[out] = res
    binary = ''
    for wire in sorted([wire for wire in storage.keys() if wire.startswith('z')], reverse=True):
        print(f'{wire}: {storage[wire]}')
        binary += str(storage[wire])
    print(binary)
    print(int(binary, 2))

# Your puzzle answer was 45121475050728.





