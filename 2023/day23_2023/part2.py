from collections import defaultdict 

input=[[c for c in line.strip()]for line in open("aoc23.txt").readlines()]
h=w=len(input)
ADJ={"^":(-1,0),"v":(1,0),"<":(0,-1),">":(0,1)}
neighbors=defaultdict(list)
dag=defaultdict(list)
split_pts=list()
s,e=(0,1),(h-1,w-2)

"""build neighbors, find the spliting pts of paths"""
for row,line in enumerate(input):
    for col,c in enumerate(line):
        if c not in ".><v^": continue
        adj=0 #adjacent 
        
        for nb in ADJ:
            dx,dy=ADJ[nb]
            nx,ny=row+dx,col+dy

            if nx<0 or nx>=h or ny<0 or ny>=w: continue
            if input[nx][ny] not in ".><v^": continue
            neighbors[(row,col)].append((nx,ny))
            adj+=1

        if adj>=3: split_pts.append((row,col))

split_pts.extend([s,e])


# for n in neighbors:
#     print(f'{n}:{neighbors[n]}')
# print(split_pts)
        
""" recursive function to return distances between splitting pts"""
def edges(curr,steps,v):
    if curr in split_pts:
        return (curr,steps)
    
    nb = [n for n in neighbors[curr] if n not in v]
    for n in nb:
        return edges(n, steps + 1, v | {curr}) 
    
# for n in neighbors[(5,3)]:
#     print(f'going to {n}')
#     t,d=edges(n,1,{(5,3)})
#     print(t,d)

global best 
best=0

"""dfs for finding longest path"""
def dfs(start,steps,v):

    if start==e:
        
        yield steps

    else:
        if start not in v:
            v.add(start)
            for nb,s in dag[start]:
                yield from dfs(nb,steps+s,v.copy())



""" buid the DAG tree"""
for pt in split_pts:
    for nb in neighbors[pt]:
        edge_pt,dist=edges(nb,1,{pt})
        dag[pt].append((edge_pt,dist))

a=dfs(s,0,set())
print(max(a))






