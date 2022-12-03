ans = 0
ans2 = 0
with open("day3\input.txt") as f:
    input = f.read().splitlines()

# part 1
for line in input:
    first_half, second_half = line[:len(line)//2],  line[len(line)//2:]
    common_bit = list(set(first_half) & set(second_half))[0]
    ans += ord(common_bit)-96 if common_bit.islower() else ord(common_bit)-38

# part 2
for x in range(0, len(input), 3):
    common_bit = list(set(input[x]) & set(input[x + 1]) & set(input[x + 2]))[0]
    ans2 += ord(common_bit)-96 if common_bit.islower() else ord(common_bit)-38

print(ans)
print(ans2)
