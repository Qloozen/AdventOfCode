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


for y in range(1, len(input)-1):
    row = input[y]
    for x in range(1, len(input[y])-1):
        col = [row[x] for row in input]
        selected = input[y][x]
        left, right, up, down = row[:x], row[x+1:], col[:y], col[y+1:]
        ans += max(left) < selected or max(right) < selected or max(up) < selected or max(down) < selected
        scenic_score = distance(selected, reversed(up)) * distance(selected, right) * distance(selected, down) * distance(selected, reversed(left))
        ans2 = scenic_score if scenic_score > ans2 else ans2

print(ans + len(input[0]) * 2 + (len(input) - 2) * 2)
print(ans2)

# Your puzzle answer was 1829
# Your puzzle answer was 291840
