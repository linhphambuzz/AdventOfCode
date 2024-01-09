from collections import defaultdict

input=open('aoc22.txt').readlines()
bricks=list()
for line in input:
    s,e=map(lambda x:x.split(","),line.strip().split('~'))
    s=[int(ss) for ss in s]
    e=[int(ee) for ee in e]
    bricks.append(s+e)
bricks.sort(key=lambda z:z[2]) #sorting with lower z
# print(bricks)

"""
    check if 2 blocks intersect 
    max(b1.x1, b2.x1) vs. min(b1.x2,b2.x2)
"""
intersect= lambda b1,b2: max(b1[0],b2[0]) <= min(b1[3],b2[3]) and \
                         max(b1[1],b2[1]) <= min(b1[4],b2[4])

""" bring the bricks down"""
for idx,brick in enumerate(bricks):
    ground=1 
    #find the ground for each brick
    for lower in bricks[:idx]:
        if intersect(brick,lower):
            ground=max(ground,lower[5]+1)

    brick[5]-=brick[2]-ground #higher end of the brick
    brick[2]=ground #lower end of the brick

bricks.sort(key=lambda z:z[2])
    
support=defaultdict(set)
supported=defaultdict(set)

for idx,b in enumerate(bricks):
    for lidx,lower in enumerate(bricks[:idx]): #traverse through lower bricks 
        if intersect(lower,b) and lower[5]+1==b[2]:
            support[lidx].add(idx)
            supported[idx].add(lidx) 

# for s in support:
#     print(f'{s} supports {support[s]}')

# for s in supported:
#     print(f'{s} is supported by {supported[s]}')


""" 
    part1: 
    safe bricks are those that  once removed, bricks that they support 
    can still be supported by others bricks 
"""

ans=0
p1=set()
for brick,_ in enumerate(bricks):
    if all(len(supported[b])>=2 for b in support[brick]): 
        p1.add(brick)
        ans+=1
print(ans)



        
"""
    part2
    bricks that got toppled over are those that: 
        - not counted in part 1
        - being supported by solely one brick    
        - BFS to traverse through bricks that get supported by bricks being supported by only one.  
"""

ans2=0
for brick,_ in enumerate(bricks):
    
    if brick not in p1: q=[brick]+[s for s in support[brick] if len(supported[s])==1] 
    v=set(q)
    # print(v)

    while q: 
        b=q.pop(0)
       
    
        for block in support[b]:
            if block in v: continue
            else: 
                if supported[block] <= v: 
                   
                    q.append(block)
                    v.add(block)
    if len(v)>1 : ans2+=len(v)-1
    
    
print(ans2)
    





