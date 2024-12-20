## Part 1

**Summary terminology:**

- register a,b,c: some global variables to store numbers.
- instructions: sequence of numbers ranging from 0 to 7.
  - opcode: the actual numbers (starting from index 0)
  - operand: the numbers next to each opcode (aka numbers on odd indexes)
    - literal operand: the number itself
    - combo operand: based on the operand number, 0-3 are also literals, 4 = value of register A, 5 = value of register B, 6 = value of register C. 7 is None.
- function pointer: the index of the current opcode

> Based on above terminology, each opcode in the list of instructions should do a certain calculation. Based on the calculation, it can change the register values, change the current function pointer, or output a certain value. Outputted values should be stored in a list. The result will be all the stored values appended together with a comma.

### approach

1. Make a while loop which runs until the pointer/index is out of bounds. NB: manually manage the pointer/index (also +2 per iteration, to always be on opcodes)
2. I created as get_combo_operand function that takes an operand number. That will return the combo version of the operand.
3. Also make a function which performs a bitwise xor operation on two given decimal numbers.
   3.1. In python use the bin() function to get the binary representation of a number.
   3.2. Make the bit strings the same length by adding zeros to the left of the shorter string. The built-in zfill() function on strings does exactly that.
   3.3. zip both strings together and perform the xor operation on each pair of bits.
   3.4. The result of the xor operation can be converted back to a decimal number using the int(string, 2) function.
4. With both functions, just make some if statements for each opcode to perform the correct operation.

## Part 2

wip
