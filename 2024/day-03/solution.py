import re
from functools import reduce

with open("input.txt") as f:
    line = f.read()
    
    # part 1
    instructions = re.findall(r"mul\(\d+,\d+\)", line)
    print(sum(reduce(lambda acc, num: acc * num,  map(int, re.findall(r'\d+', x))) for x in instructions))


    # part 2
    instructions = re.findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", line)
    result = 0
    do = True

    for instruction in instructions:
        if instruction == "do()":
            do = True
            continue
        elif instruction == "don't()":
            do = False
            continue
        
        if do: result += reduce(lambda acc, num: acc * num,  map(int, re.findall(r'\d+', instruction)))
    
    print(result)

# Your puzzle answer was 159833790
# Your puzzle answer was 89349241
        
