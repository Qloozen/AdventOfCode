import re
import copy
with open("day-05/input.txt") as f:
    input = f.read().split('\n\n')
    stacks_raw = input[0].splitlines()
    instructions = [[int(num) for num in re.findall(r'\d+', line)]
                    for line in input[1].splitlines()]

    stack_list = []
    for x in range(1, len(stacks_raw[0]), 4):
        new_stack = []
        for y in range(0, len(stacks_raw)):
            char = stacks_raw[y][x]
            if (char.isalpha()):
                new_stack.append(char)
        new_stack.reverse()
        stack_list.append(new_stack)
    p2_stack_list = copy.deepcopy(stack_list)

# part 1 & part 2
for instruction in instructions:
    amount, from_stack, to_stack = instruction[0], instruction[1] - 1, instruction[2] - 1
    
    for i in range(0, amount):
        stack_list[to_stack].append(stack_list[from_stack].pop())

    p2_stack_list[to_stack].extend(p2_stack_list[from_stack][-amount:])
    p2_stack_list[from_stack] = p2_stack_list[from_stack][:-amount]
    

ans = ''
ans2 = ''
for i in range(len(stack_list)):
    ans += stack_list[i].pop()
    ans2 += p2_stack_list[i].pop()

print(ans)
print(ans2)
# Your puzzle answer was VGBBJCRMN
# Your puzzle answer was LBBVJBRMH
