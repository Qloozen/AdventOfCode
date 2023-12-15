## Part 1

Part 1 was by far the easiest puzzle of the year. For each word like 'rn=1' you needed to do some basic operations on each character's ascii value to calculate the hash of the word. After that you sum up all the hashes and print the result.

## Part 2

Part 2 was also easy, but lots of reading and understanding the problem. Basically you have 0 -> 255 boxes, and you need to place the lenses into the correct boxes. A single input like 'rn=1' can be split up now as: 'rn': lens label, '=': operator, '1': focal_length. The whole process is as follows:

step 1: hash the lens label ('rn') the same was as part 1, this is the box number.
step 2:

- if '-': remove the lens ('rn') from the box, move other lenses in this box to the front. Nothing happens if the lens is not in the box.
- if '=':
  - if the lens is not in the box already: add the lens ('rn') with the focal_length (1) to at the end of other lenses in the box.
  - if the lens already exists in the box: replace the current focal_length with the new focal_length.

step 3: for each lens calculate the focusing power (box_number + 1) _ (lens_slot_index + 1) _ focal_length. Sum up all the focusing powers and print the result.
