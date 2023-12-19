## Part 1

It's pretty simple if you have the parsing right and the if statements right. I did it the messy way with a while loop and a bunch of if statements to follow a path, no time to clean it up yet. It could be improved with recursion.

## Part 2

So part 2 pushed me in the direction of recursion, since we now can totally ignore the parts piece of the input since we need to consider values from 1 to 4000 for each category x, m, a, s and calculate the total of combinations which are accepted. Since the amount of parts increase to $4000^4$, we cannot simply brute force it. So my theory is to go down every decision path and keep track of the ranges of each category x, m, a, s. If it reaches 'A' it should get the product of the ranges of each category and add it to the total. I think this theory is correct, but my code is not working yet.
