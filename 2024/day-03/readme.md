## Part 1

> The goal of part 1 is to find instructions from a string of characters. The instruction looks like this `mul(X,Y)`, where `X` and `Y` are integers. It needs to be exact this format, otherwise it will be ignored. To get the answer, we need to multiply `X` and `Y` of all the instructions and sum them up.

`xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))`

I used regex to find the exact mul instructions from the string.

```python
import re

line = f.read()
instructions = re.findall(r"mul\(\d+,\d+\)", line)
```

after this I used the following to calculate the sum of the instructions.

```python
print(sum(reduce(lambda acc, num: acc * num,  map(int, re.findall(r'\d+', x))) for x in instructions))
```

Above code can be broken down into the following steps.

1. `map(int, re.findall(r'\d+', x))) for x in instructions` - This finds the two numbers from each instruction and converts them into integers.

2. `reduce(lambda acc, num: acc * num, ...)` - To follow the functional programming paradigm, I used the reduce function to multiply the two numbers. You could also do this by manually access and multiply the two numbers of each instruction.

3. `sum(...)` - Finally, I used the sum function to sum up all the results from the reduce function.

## Part 2

> Part 2 introduced the `do()` and `don't()` instructions. These instructions indicate if the following mul instructions are enabled or not.

`xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))`

So i basically extended the instruction regex to include the `do()` and `don't()` instructions.

```python
instructions = re.findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", line)
```

Then manually loop over the instructions and check if the `do()` or `don't()` instruction is enabled or not. Then do the same calculation as part 1, if the `do()` instruction is enabled.

```python
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
```
