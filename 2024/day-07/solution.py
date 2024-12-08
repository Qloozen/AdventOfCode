with open("input.txt") as f:
    input = {}
    for line in f.read().splitlines():
        l, r = line.split(": ")
        input[int(l)] = list(map(int, r.split(" ")))

def generate_combinations(n):
    if n == 0: return [""]
    
    acc = generate_combinations(n - 1)

    return [combination + op for combination in acc for op in ['+', '*']]
    # return [combination + op for combination in acc for op in ['+', '*', "|"]] # uncomment part 2

ans = 0
for test_value, nums in input.items():
    combinations = generate_combinations(len(nums) - 1)

    results = []

    for combination in combinations:
        value = nums[0]
        for i, op in enumerate(combination):
            if op == "*": value *= nums[i + 1]
            elif op == '+': value += nums[i + 1]
            # else: value = int(str(value) + str(nums[i + 1])) # uncomment part 2

        results.append(value)

    if any(map(lambda res: res == test_value, results)):
        ans += test_value

print(ans)

# Your puzzle answer was 2437272016585.
# Your puzzle answer was 162987117690649.







        


        


