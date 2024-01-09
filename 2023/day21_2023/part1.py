from collections import defaultdict



input=open('aoc21.txt').readlines()
wall=set()
h,w=len(input),len(input[0].strip())

x_limit=lambda x: x>=0 and x<h 
y_limit=lambda y: y>=0 and y<w

ADJ={"n":(-1,0),"S":(1,0),"E":(0,1),"W":(0,-1)}

for row,line in enumerate(input):
    for col,c in enumerate(line.strip()):
        if c == "#": wall.add(tuple([row,col]))
        if c == "S" : sx,sy=row,col

#bfs to go to neighbors
cnt=0
q=list()
q.append([(sx,sy)])
for step in range(64):
    pts=q.pop(0)
    # print(pts)
    curr=[]
    for (x,y) in pts: 
        for nb in ADJ:
            nx,ny=ADJ[nb]
            pt=(x+nx,y+ny)  
            if pt not in wall and x_limit(pt[0]) and y_limit(pt[1]) \
            and pt not in curr: 
                curr.append(pt)
    q.append(curr)

print(len(q[0]))
                

        





        






        
            






