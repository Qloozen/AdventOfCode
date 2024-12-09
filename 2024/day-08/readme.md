## Part 1

> The goal is to find antinodes in a 2D grid of antennas. Each antenna frequency is represented by a number, a lowercase letter or a uppercase letter. An antinode occurs at any point that is perfectly in line with two antennas of the same frequence.

### Approach

1. We need to check the alignment of antenna pairs of the same frequency to find antinodes. For this I made a dictionary of antennas with their frequencies as keys and their positions as values. We can now check each pair by iterating twice over the coordinates of the antennas of the same frequency (ignoring pairs of the same antenna).

2. Then i calculate the Y and X difference between the two antennas and determine the place of the antinodes in both directions.

3. For both antinode positions from step 2, I check if that antinode is within the bounds of the grid and add it to the antinodes set.

4. Finally, print the length of the antinodes set.

## Part 2

> The antinodes can now occur at any grid position that is in line with two antennas of the same frequency. This also includes the antennas themselves (if there are more then 1 of course).

### Approach

1. I used the same code for part 1. The only difference is that we need to keep checking for other antinodes for each pair of antennas of the same frequency.

2. I wrapped the code for finding antinodes in a while loop, and keep adjusting the antinode based on the difference, and stop if it goes off grid.

3. I also did this for the other direction.

4. Finally, print the length of the antinodes set.
