from collections import defaultdict

with open("input.txt") as f:
    nums = list(map(int, f.read().split()))
    input = defaultdict(int)
    for num in nums: input[num] += 1

    for i in range(75): 
        if i == 25: print(sum(input.values()))
        updates = defaultdict(int)

        for k, v in input.items():
            s = str(k)
            updates[k] -= v

            if k == 0: 
                updates[1] += v
            elif len(s) % 2 == 0:
                l, r = s[:len(s)//2], s[len(s)//2:]
                updates[int(l)] += v
                updates[int(r)] += v
            else: 
                updates[k*2024] += v

        for k, v in updates.items():
            input[k] += v
            if input[k] == 0: input.pop(k)
       
    print(sum(input.values()))

# Your puzzle answer was 186203.
# Your puzzle answer was 221291560078593.