from functools import reduce
with open("2023\day-09\input.txt") as f: input = [list(map(int, history.split(" "))) for history in f.readlines()]

def get_hist_values(s):
    if all([x == 0 for x in s]): return (0, 0) # left (part2), right (part1)
    next_seq = [s[step+1] - s[step] for step in range(len(s)-1)]
    x = get_hist_values(next_seq)
    return (s[0] - x[0], s[-1] + x[1])
    
hist = [get_hist_values(sequence) for sequence in input]
extrapolated_values = reduce(lambda acc, x: (acc[0] + x[0], acc[1] + x[1]), hist) 
print(f"Part 1: {extrapolated_values[1]}, Part 2: {extrapolated_values[0]}")