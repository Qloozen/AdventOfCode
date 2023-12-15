## part 1

Part one was pretty straight forward. I basically move every circle to the top of the grid. and then calculate the answer, not much to say here.

## part 2

Part 2 was actually easy, but I had some reference issues....... However, I extracted the code from part 1 and made some reusable functions for moving the circles to the top and a function to calculate the total load. In part 2 one cycle is moving the circles up, left, down, right. To prevent some changes to the moving function I just rotate the whole grid.

Ofcourse they want to know the total load after 1000000000 cycles. So I try to detect a loop in the cycle-output, and use the modulo to calculate the answer for 1000000000.
