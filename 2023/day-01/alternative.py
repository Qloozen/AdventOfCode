numbers = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}
is_part_1 = True
# is_part_1 = False

with open("2023/day-01/input.txt") as f:
    ans = 0
    for line in f.read().splitlines():
        digits = []
        for i, c in enumerate(line):
            if c.isdigit(): digits.append(c)
            if is_part_1: continue        
            for key, value in numbers.items():
                if line[i:].startswith(key): digits.append(value)
        ans += int(digits[0] + digits[-1])

print(ans)
# Your puzzle answer was 56108.
# Your puzzle answer was 55652.