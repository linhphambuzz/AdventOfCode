
import re

with open("test.txt") as f:
    cubes = [tuple(map(int, re.findall("(\d+)", l))) for l in f.readlines()]

minout = [min(c[i]-1 for c in cubes) for i in range(3)]
print(minout)
maxout = [max(c[i]+1 for c in cubes) for i in range(3)]
print(maxout)