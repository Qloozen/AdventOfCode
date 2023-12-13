with open("2023\day-12\input.txt") as f: 
  input = []
  for line in f.read().splitlines():
    conditions, groups = line.split(" ")
    groups = list(map(int, groups.split(",")))
    input.append((conditions, groups))

# In progress 