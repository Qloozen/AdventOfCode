ans = []
with open("day-01/input.txt") as f:
    input = [num for num in f.read().splitlines()]

calories = 0
for line in input:
    if len(line) == 0:
        ans.append(calories)
        calories = 0
        continue
    calories += int(line)

ans.sort(reverse=True)
print(ans[0])
print(ans[0] + ans[1] + ans[2])
# Your puzzle answer was 66186
# Your puzzle answer was 196804