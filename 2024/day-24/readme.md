## Part 1

> The input has two sections, section one is a list of wires with their inital values (0 or 1). Section two contains a list of logic gates with two input wires and one output wire. Example: `wire_a AND wire_b -> wire_c` so wire_a and wire_b are inputs to the AND gate and wire_c is the output. A single wire is connected to at most one output, but can be used for many inputs. After performing all the logic gates, there will be wires listed from z00 to z.. where 00 is the least significant bit. You can construct a binary number from the z wires to get the answer.

### Approach

I keep a dictionary of wires and their values. Then I go over the list of gates to fill this dictionary. Since some inputs are not there yet, I go over this list multiple times until all the wires are filled.

In the end I construct the binary string by sorting the Z values (reverse, since 00 is the least significant bit). Then you can convert the binary string to a decimal number with `print(int(binary, 2))`

## Part 2

WIP
