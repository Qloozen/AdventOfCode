ans = 0
ans2 = 0
with open("day-09/input.txt") as f:
    input = [tuple(x.split()) for x in f.read().splitlines()]
    print(input)

head_x = head_y = 0
tail_x = tail_y = 0
visited = set()


def get_steps(start, stop, step, x, y) -> set:
    visited = set()
    for i in range(start, stop, step):
        visited.add((x if x else i, y if y else i))
    return visited


for command in input:
    direction = input[0]
    steps = int(input[1]) - 1
    if direction == 'L':
        visited.update(get_steps(tail_x, tail_x-steps, -1, None, tail_y))
        head_x -= steps
        tail_x -= steps-1
    elif direction == 'R':
        visited.update(get_steps(tail_x, tail_x+steps, 1, None, tail_y))
        head_x += steps
        tail_x += steps-1
    elif direction == 'U':
        if head_x == head_x:  # move up
            visited.update(get_steps(tail_y, tail_y+steps, 1, tail_x, None))
            head_x += steps
            tail_x += steps-1
        elif abs(head_x - tail_x) > 1 or abs(head_y - tail_y) > 1:  # check diagonal up
            is_head_left = head_x < tail_x
            if is_head_left:
                for i in range(tail_y, tail_y+(steps-1), 1):
                    visited.add((tail_x-1, i))
                tail_x -= 1
                tail_y += (head_y - tail_y)-1
            else:
                for i in range(tail_y, tail_y+(steps-1), 1):
                    visited.add((tail_x+1, i))
                tail_x += 1
                tail_y += (head_y - tail_y)-1
    elif direction == 'D':


print(ans)
print(ans2)
