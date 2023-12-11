with open("2023\day-11\input.txt") as f: input = [line for line in f.read().splitlines()]

y_expansion_points = [i for i, line in enumerate(input) if all(char == "." for char in line)]
x_expansion_points = [i for i in range(len(input[0])) if all(line[i] == "." for line in input)]

def calculate_galaxy_distances(expansion_amount):
  galaxies = []
  for y, line in enumerate(input):
    for x, char in enumerate(line):
      if char == "#":
        y_passed_points = sum(1 for ye in y_expansion_points if ye < y)
        x_passed_points = sum(1 for xe in x_expansion_points if xe < x)

        new_x = x + x_passed_points * (expansion_amount-1)
        new_y = y + y_passed_points * (expansion_amount-1)

        galaxies.append((new_y, new_x)) 

  pairs = [(galaxies[i], galaxies[j]) for i in range(len(galaxies)-1) for j in range(i + 1, len(galaxies))]

  assert len(pairs) == len(galaxies) * (len(galaxies) - 1) / 2

  total = sum(abs(pair[0][0] - pair[1][0]) + abs(pair[0][1] - pair[1][1]) for pair in pairs)

  print(total)

calculate_galaxy_distances(2)
calculate_galaxy_distances(1000000)

# Your puzzle answer was 9274989.
# Your puzzle answer was 357134560737.