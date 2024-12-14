## Part 1

> The input contains a list of robots, each having a inital position X, Y and velocity X and Y. The field is 101 wide and 103 tall. Robots can move off grid and reappear on the other side and they can also sit on the same position as another robot. After 100 moves (or 'seconds') of each robot, we need to determine how many robots there are in each quadrant of the grid and multiplying each quadrant.

```
p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3
```

### Approach

From the inital position of each robot we can multiply the velocity by 100 and add it to the initial position modulo the grid width or height. We can then count the number of robots in each quadrant (the middle lines do not count as part of any quadrant.

## Part 2

> The robots appear to form a christmas tree somewhere. We need to determine the number of seconds it takes for the robots to form the tree.

### Approach

I looked up how to print a grid as image in Python, and ran it 10.000 times. The tree is pretty obvious :).

The only adjustment I made was to 'save' the positions of every robot at every second, instead of finishing each robot at a time.

![alt text](7892.png)
