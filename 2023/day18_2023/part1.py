input=open("test.txt").readlines()
start=(0,0)
dir={"R":(0,1),"L":(0,-1),"U":(-1,0),"D":(1,0)}
tiles=set()
min_x,max_x=1000000,0
min_y,max_y=1000000,0

""" fill set with the edges """
for line in input:
    d,steps=line.split()[:2]
    for s in range(int(steps)):
        nxt=tuple([sum([curr,addx]) for curr,addx in zip(start,dir[d])])
        min_x,max_x=min(nxt[0],min_x),max(nxt[0],max_x)
        min_y,max_y=min(nxt[1],min_y),max(nxt[1],max_y)
        start=nxt
        tiles.add(nxt)


""" find start point for flood fill
    get to the mid-heigh, scan y, edge is detected is edge is 
    bw. a point inside and outside of loop, these 2 pts must
    not be included in the tiles set
"""  
start=None 
dx=min_x+(max_x-min_x)//2 
while start is None:
    for y in range(min_y,max_y+1):
        con1= (dx,y) in tiles
        con2= (dx,y-1) not in tiles and (dx,y+1) not in tiles
        if con1 and con2: 
            start=(dx,y+1)
            break
        else:
            dx+=1
            break


""" bfs  for flood fill"""

v=set()
q=[start]
while q:
    x,y=q.pop()
    if (x,y) in v:
        continue
    else:
        v.add((x,y))
        for neighbor in dir:
            new=tuple([sum([x,dir[neighbor][0]]),sum([y,dir[neighbor][1]])])
            if new not in tiles: q.append(new)
           


print(len(v)+len(tiles))



        



