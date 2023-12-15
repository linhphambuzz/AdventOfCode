import re
from collections import defaultdict
f=open('aoc18.txt').readlines()
max_sides=len(f)*6
xx=defaultdict(list)
yy=defaultdict(list)
zz=defaultdict(list)

def parse(readfile):
    ll=list()
    for line in readfile:
        x,y,z=[int(i) for i in re.findall(r'\d+',line)]
        ll.append([x,y,z])
        xx[x].append([y,z])
        yy[y].append([x,z])
        zz[z].append([x,y])
    return ll

def cover(xyz:list,coordinate:str)->int:
    count=0
    match coordinate:
        case 'x':
            point=xyz[0]
            if xyz[1:] in xx[point-1]: count+=1
            if xyz[1:] in xx[point+1]: count+=1
            return count
        case 'y':
            point=xyz[1]
            if [xyz[0],xyz[2]] in yy[point-1]: count+=1
            if [xyz[0],xyz[2]] in yy[point+1]: count+=1
            return count
        case 'z':
            point=xyz[2]
            if xyz[0:2] in zz[point-1]: count+=1
            if xyz[0:2] in zz[point+1]: count+=1
            return count
        
input=parse(f)
for cube in input:
    max_sides-=(cover(cube,'x')+cover(cube,'y')+cover(cube,'z'))
print(max_sides)







