# Part 1
with open("input.txt") as f:
    lines = [line for line in f.read().splitlines()]

    count = 0
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if j + 4 <= len(lines[i]): 
                count += lines[i][j:j+4] in ["XMAS", "SAMX"]

            if i+3 < len(lines):
                count +=''.join([lines[i+x][j] for x in range(4)]) in ["XMAS", "SAMX"]

            if i+3 < len(lines):
                ''.join([lines[i+x][j] for x in range(4)]) == "XMAS"

            count += i+3 < len(lines) and j+3 < len(lines[i]) and ''.join([lines[i+x][j+x] for x in range(4)])  == "XMAS" # bottom right 
            count += i-3 >=0 and j-3 >=0 and ''.join([lines[i-x][j-x] for x in range(4)]) == "XMAS"  # top left
            count += i+3 < len(lines) and j-3 >=0 and ''.join([lines[i+x][j-x] for x in range(4)]) == "XMAS" # bottom left
            count += i-3 >= 0 and j+3 < len(lines[i]) and ''.join([lines[i-x][j+x] for x in range(4)]) == "XMAS" # top right

    print(count)

# Part 2
with open("input.txt") as f:
    lines = [line for line in f.read().splitlines()]

    count = 0
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == 'A':
                if i-1 < 0 or j-1 < 0: continue
                if i+1 > len(lines)-1 or j+1 > len(lines[i])-1: continue

                lr = sorted([lines[i-1][j-1], lines[i+1][j+1]])
                rl = sorted([lines[i-1][j+1], lines[i+1][j-1]])

                count += lr == ['M', 'S'] and rl == ['M', 'S'] 

    print(count)

# Your puzzle answer was 2507
# Your puzzle answer was 1969






        