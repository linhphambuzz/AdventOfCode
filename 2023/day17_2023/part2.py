from heapq import heappush, heappop


input=open("input.txt").readlines()
height=len(input)
width=len(input[0].strip())
print(f'h {height} w {width}')
# assert height==width
# assert height==13

matrix=[["" for _ in range(width)]for _ in range(height)]
for r_idx,row in enumerate(input):
    for idx,i in enumerate(row.strip()): 
        matrix[r_idx][idx]=int(i)



#set up
start=(0,0) 
dest=(height-1,width-1)
compass=[(-1,0),(0,1),(1,0),(0,-1)] #n,e,s,w : 0,1,2,3
in_zone=lambda s: 0<=s[0]<height and 0<=s[1]<width
visited=set()
curr_xy=start

#queue of state (heat, coordinate,direction,mins step,max steps in same direction)\
#directions: 0->N, 1->E, 2->S, 3->W
q=[
    (0,start,1,0),
    (0,start,2,0)
]

while len(q)!=0:
    curr_state=heappop(q)
    curr_heat,curr_xy,curr_dir,curr_step=curr_state

    if (curr_xy,curr_dir,curr_step) in visited:
        continue
    else: 
        visited.add((curr_xy,curr_dir,curr_step))
        # print(curr_state)

    if curr_xy==dest and curr_step>=4: 
       print(curr_heat)
       break

    for idx,c in enumerate(compass):
        #no opposite direction 
        if idx==(curr_dir+2)%4: continue
        #next node 
        nxt_x,nxt_y=(sum(s) for s in zip(curr_xy,c))
        if not in_zone((nxt_x,nxt_y)):
            continue
        else: 
            if idx==curr_dir and curr_step<10 : 
                new_state=(curr_heat+matrix[nxt_x][nxt_y],(nxt_x,nxt_y),curr_dir,curr_step+1)
            if idx==(curr_dir+1)%4 and curr_step>=4:
                new_state=(curr_heat+matrix[nxt_x][nxt_y],(nxt_x,nxt_y),(curr_dir+1)%4,1)
            if idx==(curr_dir-1)%4 and curr_step>=4:
                new_state=(curr_heat+matrix[nxt_x][nxt_y],(nxt_x,nxt_y),(curr_dir-1)%4,1)
                    
            heappush(q,new_state)



