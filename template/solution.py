import re
from functools import reduce
from collections import defaultdict

with open("ex.txt") as f:
    lines = [line for line in f.read().splitlines()]