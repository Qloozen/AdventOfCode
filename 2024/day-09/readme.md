## Part 1

> The goal is to move file block to the empty space right to left. The disk map (input) is one large line with numbers 0-9. The numbers alternate between space file blocks and free space, aka even positions are file blocks, uneven positions are free space. The number is the amount of files blocks/ free space. File blocks can be identified by an id going left to right starting from id 0. `12345` = `0...111....22222`, where the spaces are dots and file blocks are the id's.

```
2333133121414131402
```

### Approach

I simply started by trying to re-create the disk map with the ids and spaces based on the input amounts. Once this was done, I could just swap the last file block with the first free space. Finally calculate the sum by multiplying the id of each file block with the position of the block.

It will take a little bit for the solution to run.

## Part 2

> The goal of part 2 is almost the same as part 1, only now we should not move individual file blocks, but the entire group (same id's) from right to the first available free space. If it can't fit in the free space it stays there.

### Approach

With the part 1 approach it is a bit more tricky to move blocks around. I decided to create a list of tuples (Id/Space, Amount). To have the flexibility to change the size of this map without getting issues with indexes. I used a while loop that would target the ids from the highest to the lowest. I then do a few checks to correctly move/ replace the blocks.
