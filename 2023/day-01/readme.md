## Part 1

Part one was easily done by using a regular expression to filter out all the numbers, resulting in strings like "123456". Accessing the first number with index 0 and the last number with index -1 (this also works with lists of size 1).

## Part 2

My initial setup for part 1 was not very good for part 2, because there are some overlapping numbers in the input like "oneight". To simply solve this I added the appropriate characters around the number to make sure replacing numbers would not result in cutt off words like "1ight" but instead "o1eight". Its not optimal since we need to filter out the extra characters later, but it works.

My initial thoughts was to store all indicies of the numbers but this wouldn't work on the real input. An _alternative_ approach without regex, involves a simple for loop on the line characters, keeping a list of digits and appending the character if it is an digit. To make it work for part 2, I've added an dictionary mapping for the numbers. And simply checking if the line starts with a number, from the character it is currently on.
