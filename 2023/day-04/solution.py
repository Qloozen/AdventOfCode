import re
from functools import reduce

with open("2023/day-04/input.txt") as f:
    input = []
    for line in f.read().splitlines():
      list1, list2 = line.split(": ")[1].split("|")
      winning_numbers, numbers = set(re.split('\s+', list1.strip())), set(re.split('\s+', list2.strip()))
      input.append((1, winning_numbers, numbers))

def make_copies(start, amount):
  for j in range(0, amount):
    if start + j >= len(input): break
    card = input[start + j]
    input[start + j] = (card[0] + 1, card[1], card[2])

ans = 0
for i, (amount, winning_numbers, numbers) in enumerate(input):
  intersection_amount = len(winning_numbers & numbers)
  ans += 0 if intersection_amount == 0 else 2 ** (intersection_amount - 1)
  for j in range(amount): make_copies(i+1, intersection_amount) # part 2

ans2 = reduce(lambda acc, card: acc + card[0], input, 0)

print(ans)
print(ans2)