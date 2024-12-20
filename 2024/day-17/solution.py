import re
from functools import reduce
from collections import defaultdict, Counter

with open("input.txt") as f:
    registers, instructions = f.read().split('\n\n')
    registers = registers.splitlines()
    
    a = int(registers[0].split(': ')[1])
    b = int(registers[1].split(': ')[1])
    c = int(registers[2].split(': ')[1])

    instructions = list(map(int, instructions.split(': ')[1].split(',')))

    def get_combo_operand(operand):
        if 0 <= operand <= 3: return operand
        elif operand == 4: return a
        elif operand == 5: return b
        elif operand == 6: return c
        else: return None
    
    def get_bitwise_xor(a, b):
        bin_a = bin(a)[2:]
        bin_b = bin(b)[2:]
        length = max(len(bin_a), len(bin_b))
        bin_a = bin_a.zfill(length)
        bin_b= bin_b.zfill(length)

        xor = zip(bin_a, bin_b)
        result = ''
        for a, b in xor:
            if a == '1' and b == '1' or a == '0' and b == '0':
                result += '0'
            else:
                result += '1'
        decimal = int(result, 2)
        return decimal

    
    pointer = 0
    output = []
    while pointer < len(instructions):
        opcode = instructions[pointer]
        operand = instructions[pointer + 1]
        combo_operand = get_combo_operand(operand)

        if opcode == 0: # adv
            if combo_operand == None: continue
            a = a // 2**combo_operand
        elif opcode == 1: # bxl
            b = get_bitwise_xor(operand, b)
        elif opcode == 2: # bst
            if combo_operand == None: continue
            b = combo_operand % 8
        elif opcode == 3: #jnz
            if a != 0: 
                pointer = operand
                continue
        elif opcode == 4: #bxc
            b = get_bitwise_xor(b, c)
        elif opcode == 5: # out
            if combo_operand == None: continue
            output.append(combo_operand % 8)
        elif opcode == 6: #bdv
            if combo_operand == None: continue
            b = a // 2**combo_operand
        elif opcode == 7:
            if combo_operand == None: continue
            c = a // 2**combo_operand
        
        pointer += 2
    print(','.join(map(str, output)))



 



