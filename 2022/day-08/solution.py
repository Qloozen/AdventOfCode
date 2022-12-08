ans = 0
ans2 = 0
with open("day-08/input.txt") as f:
    input = [[int(num) for num in line] for line in f.read().splitlines()]


def distance(selected, arr) -> int:  # Part 2
    viewing_distance = 0
    arr = list(arr)
    for i in range(len(arr)):
        viewing_distance += 1
        if arr[i] >= selected:
            return viewing_distance
    return viewing_distance


for y_index, row in enumerate(input):
    if y_index == 0 or y_index == len(input) - 1:
        continue
    for x_index, x in enumerate(row):
        if x_index == 0 or x_index == len(row) - 1:
            continue
        col = [row[x_index] for row in input]
        left, right, up, down = row[:x_index], row[x_index+1:], col[:y_index], col[y_index+1:]
        is_visable = max(left) < x or max(
            right) < x or max(up) < x or max(down) < x
        ans += is_visable
        scenic_score = distance(x, reversed(up)) * distance(x, right) * distance(x, down) * distance(x, reversed(left))
        ans2 = scenic_score if scenic_score > ans2 else ans2

print(ans + len(input[0]) * 2 + (len(input) - 2) * 2)
print(ans2)
