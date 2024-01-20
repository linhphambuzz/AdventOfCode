
from collections import defaultdict
import heapq

""" improvise the solution for optimal computing time using dijkstra's """

d=defaultdict(int)
input=open('aoc21.txt').readlines()
wall=set()
h,w=len(input),len(input[0].strip())
assert h==131
ADJ={"n":(-1,0),"S":(1,0),"E":(0,1),"W":(0,-1)}
#check limit 
x_limit=lambda x: x>=0 and x<h 
y_limit=lambda y: y>=0 and y<w
not_wall=lambda x,y: input[x%h][y%w]!='#'

# print(h,w)
for row,line in enumerate(input):
    for col,c in enumerate(line.strip()):
        if c == "#": wall.add(tuple([row,col]))
        if c == "S" : sx,sy=row,col
# print(sx,sy)
d[(sx,sy)]=0

"""
    dijkstra:  at each points, values calculated is the smallest numbers of
    steps needed for that point to be filled 
    the map can be extended infinitely, allocate 
"""
for x in [-i for i in range(h*4+1)][1:] +list(range(h*4+1)):
    for y in [-i for i in range(w*4+1)][1:] +list(range(w*4+1)):
        if not_wall(x,y): d[(x,y)]=100000

v=set()
q=[]
heapq.heappush(q,(0,(sx,sy)))

while q: 

    steps,(x,y)=heapq.heappop(q)
    # print(steps,x,y)
    if steps==328: 
        continue
    if (x,y) in v:
        continue
    else: 
        v.add((x,y))
        steps+=1 

        for nb in ADJ: 
            dx,dy=ADJ[nb]
            nx,ny=x+dx,y+dy
            if not_wall(nx,ny):
                if d[(nx,ny)]>steps:
                    d[(nx,ny)]=steps
                heapq.heappush(q,(steps,(nx,ny)))


   


""" 
    64 steps: 64 is an even numbers 
    Total of titles filled after 64 steps is numbers of titles
    that costs an even number of steps to reach to, these even numbers 
    of steps are less than or equal to 64


"""
cnt=0
a=[co for co,v in d.items() if v in [i for i in range(65)[0::2]]]


print(len(a))

# for dd in d:
#     print(f' {dd}: {d[dd]}')

        
        


