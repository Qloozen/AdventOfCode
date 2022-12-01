with open("day1\input.txt") as f:
    elves = [[elve for elve in line.splitlines()] for line in f.read().split('\n\n')]
    sum_elves = sorted([sum(list(map(int, x))) for x in elves], reverse=True)
print(sum_elves[0])
print(sum_elves[0] + sum_elves[1] + sum_elves[2])
