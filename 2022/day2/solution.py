ans = 0
ans2 = 0
with open("day2/input.txt") as f:
    input = [tuple(line.split()) for line in f.read().splitlines()]

# A  = rock, B = paper, C = scissors
# X = rock, Y = paper , Z = scissors
opponent_wins = {'A': 'Z', 'B': 'X', 'C': 'Y'}
points = {'X': 1, 'Y': 2, 'Z': 3}
draw = {'A': 'X', 'B': 'Y', 'C': 'Z'}

for move in input:
    ans += points[move[1]]
    if draw[move[0]] == move[1]:
        ans += 3
    elif opponent_wins[move[0]] != move[1]:
        ans += 6

# part 2
opponent_loses = {'A': 'Y', 'B': 'Z', 'C': 'X'}
for move in input:
    if move[1] == 'X':
        ans2 += 0
        should_pick = opponent_wins[move[0]]
        ans2 += points[should_pick]
    elif move[1] == 'Y':
        ans2 += 3
        should_pick = draw[move[0]]
        ans2 += points[should_pick]
    elif move[1] == 'Z':
        ans2 += 6
        should_pick = opponent_loses[move[0]]
        ans2 += points[should_pick]

print(ans)
print(ans2)
