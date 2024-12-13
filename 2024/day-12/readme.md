## Part 1

> The input consist of garden plots with different types of plants, which are grouped in a 2D array. The goal is to find the cost of the fence that surrounds the garden. the cost is calculated by multiplying the number of plants (area) in the garden by the perimeter of the garden. Plants of the same type can appear in separate regions. Finally we need to sum up the cost of all regions.

### Approach

I've done part one with a queue, but this could also be done with some recursion. For each plant in a region I simply determine if the directions: up, right, down, left are out of bounds or does not contain the same plant. Then we know that place should be a fence.

## Part 2

> In the second part the cost is calculated by multiplying the area by the number of sides.

### Approach (not finished)

My approach was to find the number of corners. Corners are plants that have at least 2 fences next to it. 2 fences would equal to 1 corner, 3 fences would equal to 2 corners and 4 fences would equal to 4 corners. We also need to find the inward corners. To find inward corners I store the plants around the current region. The amount of times a plant is found in the surrounding area is the amount of fences it touches. This also means 2 fences = 1 side, 3 fences = 2 sides and 4 fences = 4 sides.

There are two catches. The first one is that 2 fences does not always equal 1 corner. If the region is one wide or tall, it could mean the fences are parralel from eachother, so this would not count as a corner.

The second catch is also with 2 fences. If there is a region in another region, there could be a corner in the middle of the region. This would conflict with counting as a corner and a inwards corner, resulting in a too large number of sides. Still need this fix this one..
