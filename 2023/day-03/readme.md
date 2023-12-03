## Part 1

First I extracted the symbols from the input file, which are non-digits and not a dot (note that the example and the input have different symbols):

```python
SYMBOLS = set([char for line in input for char in line if not char.isdigit() and char != '.'])
```

After that I looped over all the characters of each line, keeping track of the current number by appending the digits to a string. After reaching a new dot or the end of the line, the digit is checked if it is a engine part or not. After each digit the values are reset. At the end we sum all the engine parts.

# Part 2

To find the gears that are connected to two part numbers, I added a dictionary with the (x, y) tuple of each gear. The dictionary might look like this:

```python
# gear coords: [part numbers]
{
    (0, 2): [123, 456],
    (10, 15): [123],
}
```

While finding the part numbers I keep track of all the connected gears, a `set()` is used to prevent duplicate gears for a single part number. After the part number is found and all connected gears are known, we add the part number to the corresponding gears in the dictionary.

At last we can use the reduce function to get the gear ratio for all gears that have 2 connected part numbers.
