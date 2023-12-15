import re
from collections import defaultdict

with open("2023\day-15\input.txt") as f:
  input = f.read().split(",")

def hash(word):
  hash_code = 0
  for char in word:
    val = ord(char)
    hash_code = ((hash_code + val) * 17) % 256
  return hash_code

# part 1
print(sum(hash(s) for s in input))

# part 2
boxes = defaultdict(list)

for line in input:
  label, operation, focal_length = re.split(r'(=|-)', line)
  box_id = hash(label)
  
  if operation == "=":
    focal_length = int(focal_length)
    
    if any(label == lens[0] for lens in boxes[box_id]):
      for i, lens in enumerate(boxes[box_id]):
        if lens[0] == label:
          boxes[box_id][i] = (label, focal_length)
          break
    else:
      boxes[box_id].append((label, focal_length))

  if operation == "-":
    for i, lens in enumerate(boxes[box_id]):
      if lens[0] == label:
        boxes[box_id].pop(i)
        break

focusing_power = 0    
for box_id, lenses in boxes.items():
  for i, (_, focal_length) in enumerate(lenses):
    focusing_power += (box_id + 1) * (i + 1) * focal_length

print(focusing_power)

# Your puzzle answer was 513643.
# Your puzzle answer was 265345.