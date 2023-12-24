import re 
from collections import defaultdict,namedtuple

"""
Using pick's theorem  https://en.wikipedia.org/wiki/Pick%27s_theorem
to establish the relation between area, border points and inside points 
        A=i+b/2-1 
        =>i+b=A+b/2+1
"""
tracks=defaultdict(set)
input=open('aoc18.txt').readlines()
dir={0:"R",1:"D",2:"L",3:"U"}
co=namedtuple("co",["x","y"])
start=co(0,0) 
area=0
border=0


for line in input:
    _,_,i=line.split()
    i=re.findall(r'\w+\d+',i)[0]
    steps,d=int(i[:len(i)-1],16),int(i[-1])
    # steps=int(steps)
    border+=steps

    match dir[d]:
        case "R":
            pt=co(start.x,start.y+steps)
        case "L":
            pt=co(start.x,start.y-steps)
        case "U":
            pt=co(start.x-steps,start.y)
        case "D":
            pt=co(start.x+steps,start.y)
    
    area+=start.x*pt.y-pt.x*start.y
    start=pt

area+=start.x-start.y


print(abs(area)//2+border//2+1)







    
   
    
