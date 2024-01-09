""" 
    This solution is based off of the geometry explanation in this wiki: 
    https://github.com/villuna/aoc23/wiki/A-Geometric-solution-to-advent-of-code-2023,-day-21
    
"""
from collections import defaultdict
import heapq

""" improvise the solution for optimal computing time using dijkstra's """

d=defaultdict(int)
input=open('aoc21.txt').readlines()
wall=set()
h,w=len(input),len(input[0].strip())
ADJ={"n":(-1,0),"S":(1,0),"E":(0,1),"W":(0,-1)}
#check limit 
x_limit=lambda x: x>=0 and x<h 
y_limit=lambda y: y>=0 and y<w

# print(h,w)
for row,line in enumerate(input):
    for col,c in enumerate(line.strip()):
        if c == "#": wall.add(tuple([row,col]))
        if c == "S" : sx,sy=row,col

d[(sx,sy)]=0

#dijkstra

for x in range(h):
    for y in range(w):
        if (x,y) not in wall: d[(x,y)]=100000

v=set()
q=[]
heapq.heappush(q,(0,(sx,sy)))

while q: 

    steps,(x,y)=heapq.heappop(q)
    # print(steps,x,y)
    if (x,y) in v:
        continue
    else: 
        v.add((x,y))
        steps+=1 

        for nb in ADJ: 
            dx,dy=ADJ[nb]
            nx,ny=x+dx,y+dy
            if (nx,ny) not in wall and x_limit(nx) and y_limit(ny):
                if d[(nx,ny)]>steps:
                    d[(nx,ny)]=steps
                heapq.heappush(q,(steps,(nx,ny)))
    

cnt=0
a=[co for co,v in d.items() if v in [i for i in range(66)[2::2]]]

print(len(a))


        
        


