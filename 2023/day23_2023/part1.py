from collections import defaultdict 
import time
import sys 

sys.setrecursionlimit(10000)

input=[[c for c in line.strip()]for line in open("test.txt").readlines()]
h=w=len(input)
ADJ={"^":(-1,0),"v":(1,0),"<":(0,-1),">":(0,1)}
d=defaultdict(int)

forest=lambda x,y: input[x][y]=="#"
slopes=lambda x,y: input[x][y] in ["<",">","^","v"]
limit=lambda x,y: x in range(h) and y in range(w)

for row,line in enumerate(input):
    for col,c in enumerate(line):
        if row==0 and c==".": 
            s=(row,col)
           
        elif row==h-1 and c==".": 
            e= (row,col)

def get_nb(node):
    x,y=node
    if input[x][y] in "^v<>":
        
            
def dfs(start,steps,v):
    if start==e: 
        yield steps
    else:
        
        if start not in v:
            v.add(start)   
            x,y=start
            if input[x][y] in "^v<>":
                dx,dy=ADJ[input[x][y]]
                yield from dfs((x+dx,y+dy),steps+1,v.copy())

            else:
                for nb in ADJ:
                    dx,dy=ADJ[nb]
                    nx,ny=x+dx,y+dy
                    if limit(nx,ny) and not forest(nx,ny):
                        yield from dfs((nx,ny),steps+1,v.copy())
  

a=dfs(s,0,set())
print(max(list(a)))



        











