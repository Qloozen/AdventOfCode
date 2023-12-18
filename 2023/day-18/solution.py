with open("ex.txt") as f:
  input = f.read().splitlines()

def parse(input, part=1):
  edges = [(0, 0)]
  border_length = 0

  for line in input:
    direction, val, color = line.split()
    val = int(val)
    if part == 2:
      direction = color[-2]
      val = int(color[2:7], 16)

    last_edge = edges[-1]
    if direction in ['R', '0']: 
      edges.append((last_edge[0], last_edge[1] + val))
      border_length += val
    if direction in ['L', '2']: 
      edges.append((last_edge[0], last_edge[1] - val))
      border_length += val
    if direction in ['U', '3']: 
      edges.append((last_edge[0] - val, last_edge[1]))
      border_length += val
    if direction in ['D', '1']: 
      edges.append((last_edge[0] + val, last_edge[1]))
      border_length += val
  return edges, border_length

def calculate_surface(edges):
  # https://www.101computing.net/the-shoelace-algorithm/
  # To apply the shoelace algorithm you will need to:
  #     List all the vertices in anticlockwise order. (e.g. A,B,C,D,E) in a table, and note the x and y coordinates in two separate columns of the table,
  #     Calculate the sum of multiplying each x coordinate with the y coordinate in the row below (wrapping around back to the first line when you reach the bottom of the table),
  #     Calculate the sum of multiplying each y coordinate with the x coordinate in the row below (wrapping around back to the first line when you reach the bottom of the table),
  #     Subtract the second sum from the first, get the absolute value (Absolute dfference |sum1-sum2|,
  #     Divide the resulting value by 2 to get the actual area of the polygon.

  a, b = 0, 0
  for i in range(len(edges) -1):
    a += edges[i][0] * edges[i + 1][1]
    b += edges[i][1] * edges[i + 1][0]
  
  surface = (abs(a - b) / 2)

  # Pick theorem to calculate the area https://en.wikipedia.org/wiki/Pick%27s_theorem
  interior_points =  surface - border_length // 2 + 1

  print(round(interior_points + border_length))

edges, border_length = parse(input, part=1)
calculate_surface(edges)

edges, border_length = parse(input, part=2)
calculate_surface(edges)

# Your puzzle answer was 44436.
# Your puzzle answer was 106941819907437.