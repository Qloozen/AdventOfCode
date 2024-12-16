## Part 1

> The input contains a 2D grid with a robot (@), boxes (O), walls (#) and empty space (.). The input also contains a sequence of instructions the robot follows: '^v<>'. The robot can push a box if it is not against a wall, it can move multiple boxes at the same time. After the whole instruction sequence has run, we need to calculate the GPS coordinates of all boxes and sum them up. A GPS coordinate of a box is equal to 100 times its distance form the top edge plus its distance from the left edge.

```
########
#..O.O.#
##@.O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

<^^>>>vv<v>>v<<
```

### Approach

Part 1 is quite straightforward. I just move the robot inside the 2D grid. If the robot encounters a box I am looking for a empty space in the direction the robot wants to move. If there is an empty space along the way, I move the first box to that empty space. This way I am not shifting each box one by one, if there are more.

Finally I calculate the GPS coordinates of all boxes and sum them up. The distance from the top and left can be seen as the coordinates of the box.

## Part 2

> The grid gets twice as wide. The rules from part 1 still apply.

- If the tile is #, the new map contains ## instead.
- If the tile is O, the new map contains [] instead.
- If the tile is ., the new map contains .. instead.
- If the tile is @, the new map contains @. instead.

### Approach

There are a few things to consider in part 2. One is that boxes are now two wide, there will be situations were boxes are partially stacked on top of each other. Two, we need to move two pieces '[' and ']' now. And three, we can't place the first box to the first open space we encounter, like part 1.

1. I convert the input to follow above rules.
2. Check if the next move is a box (either '[' ']')
3. For each box, I check if there is a box connected to it. I use a queue to go over all of them.
4. I also store the boxes in the array seen (in order). This way if the boxes can be moved, I can move them in reverse order.
5. If any of the boxes has a wall in front of it, I switch the can_move flag to False.
6. If the can_move flag is True, I move the boxes to the next open space.
