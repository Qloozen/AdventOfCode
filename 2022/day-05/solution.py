import re
ans = 0
ans2 = 0
with open("day-05/input.txt") as f:
    input = f.read().split('\n\n')
    stacks_raw = input[0].splitlines()
    instructions = [[int(num) for num in re.findall(r'\d+', line)]
                    for line in input[1].splitlines()]

    stack_list = []
    # print(input[0])
    for x in range(1, len(stacks_raw[0]), 4):
        new_stack = []
        is_stack = False
        for y in range(0, len(stacks_raw)):
            char = stacks_raw[y][x]
            if (char.isalpha()):
                new_stack.append(char)
                is_stack = True
        if is_stack:
            new_stack.reverse()
            stack_list.append(new_stack)

    p2_stack_list = stack_list.copy()
    for instruction in instructions:
        amount, from_stack, to_stack = instruction[0], instruction[1] - \
            1, instruction[2] - 1

        for i in range(0, amount):
            stack_list[to_stack].append(stack_list[from_stack].pop())

        t = p2_stack_list[from_stack][-amount:]
        p2_stack_list[to_stack].append(p2_stack_list[from_stack][-amount:])

    ans = ''
    for stack in stack_list:
        ans += stack.pop()
    print(ans)
