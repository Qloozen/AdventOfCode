## Part 1

> The input consist of garden plots with different types of plants, which are grouped in a 2D array. The goal is to find the cost of the fence that surrounds the garden. the cost is calculated by multiplying the number of plants (area) in the garden by the perimeter of the garden. Plants of the same type can appear in separate regions. Finally we need to sum up the cost of all regions.

### Approach

I've done part one with a queue, but this could also be done with some recursion. For each plant in a region I simply determine if the directions: up, right, down, left are out of bounds or does not contain the same plant. Then we know that place should be a fence. I also return the visited set of each region. This is nice to have for part 2.

## Part 2

> In the second part the cost is calculated by multiplying the area by the number of sides.

### Approach

You can state that the number of sides is equal to the number of corners. If a plant (square) has 2 fences it either forms a corner or forms 2 parallel fences (which is not a valid corner). `ex3.txt` helped me to find this issue. If a plant has 3 fences it is sticking our of its region, forming 2 corners. If a plant has 4 fences, then the plant itself is the region, so it has 4 corners. So these rules I followed:

- 1 fence = 0 corners (part of a straight line)
- 2 fences = 1 corner if not parallel
- 3 fences = 2 corners
- 4 fences = 4 corners

So one fail case were the parallel fences, which I fixed by checking if the direction of the fences are not opposite. The other fail case was on example `ex4.txt`. Here you have two B regions inside the A region. The problem arises when two A plants are diagonally connected _in the center_, both with a B plant next to it. Both A plants and B plant (diagonally of eachother) will count 2 corners for region A, causing 2 extra corners.

To fix this I keep track of diagonal connections. And removing 2 corners of a region if it has a diagonal connection with a plant in the same region. One small error I made was to not include a diagonal block multiple times, so if a plant has 2 or more diagonal connections, it didn't remove 2 corners for each pair of diagonals. I found this with the `edgecase.txt` example.

_No, I am not going to optimize this solution.._
