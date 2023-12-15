from collections import defaultdict 
import re 

from part1 import getNeighbor

input=open("aoc3.txt").readlines()
stars=set()
numbers=defaultdict(int)
stars_track=defaultdict(list)

gearRatio=lambda n:n[0]*n[1]

for line_idx,line in enumerate(input):
    line.strip()
    all_num=re.findall(r'\d+',line)
    idx_num=[(i.start(0),i.end(0)) for i in re.finditer(r'\d+',line)]
    numbers.update({(line_idx,idx):int(n) for n,idx in zip(all_num,idx_num)})
# get all *
    s_idx=[i.start(0) for i in re.finditer(r'\*',line)]
    for s in s_idx:
        if s: stars.add((line_idx,s))


for n in numbers:
    row,(col,end_idx)=n 
    neighbors=getNeighbor(row,col,end_idx)
    for nb in neighbors:
        if nb in stars:
            stars_track[nb].append(numbers[n])

result=0
for star in stars_track:
    if len(stars_track[star])>1: result+=gearRatio(stars_track[star])

print(result)



            

