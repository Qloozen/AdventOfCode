## Part 1

> The input consist of claw machines. Each machine has button A and button B. A single press on a button will move the X and Y coordinates by the amount of the button. The cost of a single press for button A is 3 and 1 for button B. The machine pize is at a specific X, Y location. The goal is to find the minimum cost to reach the prize.

### Approach

1. I search for every possible ways how the X target can be reached by pressing button A and B. The outer for loop is for button A and the inner loop is for button B.
2. Once I have a list of possible ways to reach the X target, I sort the list by the cost.
3. For each option I check if this would also reach target Y. If it does, I sum up the cost

## Part 2

> The targets (X and Y) have increased by 10000000000000.

### Approach

idk.

I guess there is a easier way to solve this by using math. My solution will never work for the increased target.
