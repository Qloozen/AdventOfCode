## Part 1

> The goal is to find hiking trails in a 2D grid. A hiking trail is a path that start at 'height' 0 and ends at 9, with steps not larger then 1. The start '0' is also called a trail head. Finally we need to find the score of each trailhead in the grid. The score of a trail head is the number of 9-height positions reachable from the trail head.

### Approach

1. **Find all starting points (trail heads) in the grid.**
   I started by parsing the input as a 2D grid while also finding all the trail heads and storing their positions in a list.

2. **This problem can be solved using a queue for each starting position.**
   Each iteration I look in all 4 directions (up, right, down, left) and check if the next position is within the grid and if the step is not larger or smaller then 1. If that is the case we either find a new step towards the trail end '9' or we are currently at the end of the trail. If we are at a new step at that position to the queue. If we are at the end of the trail we increase the score of the trail head (starting position).

   > Since part 1 is about how many ends it can reach and not necessarily the amount of possible ways it can reach the end, I keep track of the trail end positions already found.

3. Finally add up all the scores of each head trail.

## Part 2

> The goal of part 2 is to find all the possible paths to the end for each trail head, which is now the score of the trail head.

### Approach

Since we did all the work in part 1. We just need to get rid of the `seen` trail ends ('9') check. This way we can find all the possible paths to the end for each trail head.

_I actually had this before I got part 1 working hehe_
