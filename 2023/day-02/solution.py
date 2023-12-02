RED = "red"
BLUE = "blue"
GREEN = "green"

maximum = {
    RED: 12,
    GREEN: 13, 
    BLUE: 14,
}

with open("2023/day-02/input.txt") as f:
    # Game 1 structure:
    # 1: [{'blue': 3, 'red': 4}, {'red': 1, 'green': 2, 'blue': 6}, {'green': 2}]
    input = {}
    for line in f.read().splitlines():
        game_name, data = line.split(": ")
        game_id = int(game_name.split(" ")[1])

        game_sets = []
        for s in data.split("; "):
            game_set = {}
            for cubes in s.split(", "):
                val, color = cubes.split(" ")
                game_set[color] = int(val)
                
            game_sets.append(game_set)
        input[game_id] = game_sets

ans = 0
ans_2 = 0
for game_id, game_sets in input.items():
    game_valid = True;
    fewest_cubes = {RED: 0, GREEN: 0, BLUE: 0} # part 2
    for game_set in game_sets:
        for color, val in game_set.items():
            fewest_cubes[color] = max(fewest_cubes[color], val) # part 2
            if val > maximum[color]:
                game_valid = False

    ans_2 += fewest_cubes[RED] * fewest_cubes[GREEN] * fewest_cubes[BLUE] # part 2
    ans += game_id if game_valid else 0

print(ans)
print(ans_2)

# Your puzzle answer was 2771.
# Your puzzle answer was 70924.