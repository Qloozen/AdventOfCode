## Part 1

> The input is a list of numbers or 'stones'. Each blink or simply a single iteration, will cause the entire list of numbers to change following the rules below:

- 0 becomes 1
- Even numbers are split into two numbers 5000 -> 50 and 00
- Any other number gets multiplied by 2024

The description tells us the order need to be preserved. But this actually doesn't impact the result. Finally the answer is the length of the list of stones after 25 blinks.

### Solution

Since I started off by just following the rules and changing the list of numbers, which is quite easy to do. I used a while loop and manual a manual index to alter the input list while iterating over it.

```python
with open("input.txt") as f:
    input = list(map(int, f.read().split()))

    for _ in range(25):
        i = 0
        while i < len(input):
            s = str(input[i])

            if input[i] == 0: input[i] = 1
            elif len(s) % 2 == 0:
                l, r = s[:len(s)//2], s[len(s)//2:]
                input[i] = int(r)
                input.insert(i, int(l))
                i+=1
            else:
                input[i] *= 2024
            i+=1
    print(len(input))
```

## Part 2

> The goal is simple, we need to increase the blinks to 75. But the main challenge is the complexity of this problem. Simply by using above approach, it will take a lot of time to compute the result. The input gets massive. A different approach is needed

### Solution

I struggled a lot by finding a right solution for this. But after I printed out the list from part 1, I quickly noticed most of the numbers in the list are duplicates. So I decided to use a dictionary to store the numbers and their counts. This way I can reduce the complexity of the problem.

The only change needed is to update the input to a dictionary and the updates to a dictionary and then count the sum of the values in the dictionary.

```python
from collections import defaultdict

with open("input.txt") as f:
    nums = list(map(int, f.read().split()))
    input = defaultdict(int)
    for num in nums: input[num] += 1

    for _ in range(75): # change to 25 for p1
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
```
