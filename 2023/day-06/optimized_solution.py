import re
import math

with open("2023/day-06/input.txt") as f:
   nums = re.findall(r'\d+', f.read())
   races = zip(list(map(int, nums[:len(nums)//2])), list(map(int, nums[len(nums)//2:])))

def find_possible_records(max_time, record):
  for hold in range(0, max_time+1):
    distance = hold * (max_time - hold)
    if distance > record:
      range_end = max_time - hold
      range_length = (range_end - hold) + 1
      return range_length

# Part 1
records_per_game = [find_possible_records(max_time, record) for max_time, record in races]
print(math.prod(records_per_game))  

# Part 2
max_time = int("".join(nums[:len(nums)//2]))
record = int("".join(nums[len(nums)//2:]))
print(find_possible_records(max_time, record))

# Your puzzle answer was 275724.
# Your puzzle answer was 37286485.