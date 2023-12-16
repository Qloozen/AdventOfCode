# Part 1

I initially made a recursive function to solve part 1, it worked, but only for the example. While debugging I encountered a maximum recursion depth error, so I rewrote the current code to a queue. This also only worked for the example. After looking though all the ugly if statements I came to the conclusing that I should start at index -1 instead of moving from 0. It failed because the first tile in my input was a '\', which would be skipped if I started from 0... :(

So I basically work with (position_y, position_x, direction_y, direction_x) tuples. These tuples are added to the queue and also to the visited set. The puzzle contains loops so that is why I include the direction with the position. The characters/splitters "|" and "-", will be the cause of starting a loop, thats why we check if the current position is in the visited set.

# Part 2

I wrapped my whole part 1 in a function and called it from the border of the input. Top to bottom, bottom to top, left to right and right to left.
