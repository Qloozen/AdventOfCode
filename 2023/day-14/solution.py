with open("2023\day-14\input.txt") as f: 
  input = [[char for char in line] for line in f.read().splitlines()]
  

for x in range(len(input[0])):
  top = 0
  for y in range(len(input)):
    a = input[y][x]
    if a == '.': continue
    if y == 0 or a == '#' or input[y-1][x] in ['O', '#']:
      top = y+1
      continue
    input[y][x] = '.'
    input[top][x] = 'O'
    top += 1

total_load = 0

for i, line in enumerate(input):
  load = len(input) - i
  total_load += sum(load for char in line if char == 'O')
    
print(total_load)
  