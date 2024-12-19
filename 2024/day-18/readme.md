## Part 1

> Given a list of byte coordinates, we need to find a way though a 2D grid of 71 by 71. The start is always at 0,0 and the end is bottom right at 70,70. We cannot step on the bytes. The goal is to find the minimum steps needed to reach the end by only using the first 1024 bytes in the list.

### Approach

Finding the shortest path in a 2D grid can be solved using breadth-first search. Each iteration we will check all possible directions one by one (aka, layer by layer). This way we can ensure that the first path we find is the shortest.

The visted or seen set is needed if two paths lead to the same cell. We also check if the next cell is not already in the queue, this can happen if two cells at the same distance have the same neighbor.

On each cell I store the distance from the start. This way we get the answer when we reach the end.

## Part 2

> In part 1 we checked the grid using only the first 1024 bytes (blocks were we can't step on). In part two the goal is to find how many bytes are needed to make the end unreachable. The answer will be the coordinates of the first byte that makes the end unreachable.

### Approach

My first approach was to brute force the solution. I fed my BFS method with different lengths of the byte list until the end was unreachable. Of course starting from 1024, since part 1 already indicated this amount of bytes would not block the end.

My revised approach was to use depth-first search + binary search to find the answer. Breadth-first searches every node until it finds the end, this is especially good if you already know the end is closer to the start. The answer lies all the way at the end, so depth-first search is better for this solution, also because we don't care about if it is the shortest path.

Altough DFS is faster then BFS, it is still slow. So I used binary search to find the answer quicker. This way we can skip alot of iterations.
