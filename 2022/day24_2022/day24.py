from math import lcm
from heapq import heappop,heappush
input=open('aoc24.txt').readlines()
given_map=[line.strip() for line in input]
max_row=len(given_map)
max_col=len(given_map[0])
states=lcm(max_row-2,max_col-2)

def get_neighbor(coor):
    nb=list()
    x,y=coor
    x_u,x_d,x=[x-i for i in [1,-1,0]]
    y_l,y_r,y=[y-i for i in [1,-1,0]] 
    return [(x,yn) for yn in [y_l,y_r,y]]+[(xn,y) for xn in [x_u,x_d]]

current_snow= set((x,y,given_map[x][y]) for x in range(max_row) for y in range(max_col)
                  if given_map[x][y] not in ['#','.'])

MOVE={'>':(0,1),'<':(0,-1),'^':(-1,0),'v':(1,0)}
#method to move the snow every minute passed by 
def move_snow(curr):
    new_snow=set()
    for snow in curr:
        x,y,dir=snow
        new_x=x+MOVE[dir][0]
        new_y=y+MOVE[dir][1]
        if new_x==max_row-1: new_x=1
        if new_x==0: new_x=max_row-2
        if new_y==max_col-1: new_y=1
        if new_y==0: new_y= max_col-2
        new_snow.add((new_x,new_y,dir))
    return new_snow

#dictionary to look up for map corresponding to each state
#this map represents all occupied coordinate 
map_states={s:set() for s in range(states)}
for s in range(states):
    next=move_snow(current_snow)
    current_snow=next
    for snow in next:
        snow=snow[:-1]  #elimiate direction of the snow  
        map_states[s].add(snow)

def part1(start):
    queue=list()
    visit=set()
    #cursor=(0,1)
    dest=(max_row-1,max_col-2)
    #print(dest)
    time=0
    heappush(queue,(time,start))
    
    while queue: 
        if not queue: break 
        
        time,cursor=heappop(queue)
        if cursor==dest: return time
        s=time%states
        map=map_states[s]
        
        if (s,cursor) not in visit: 
            visit.add((s,cursor))
            #if cursor==dest: return time
            for n in get_neighbor(cursor):
                nx,ny=n
                if 0<nx<max_row-1 and 0<ny<max_col-1 or (nx,ny) in [start,dest]:
                    if n not in map:
                        #print(nx,ny)
                        heappush(queue,(time+1,n))
                             
    return time       

t1=part1((0,1))

def part2(start,dest,start_time): 
    queue=list()
    visit=set()
    time=start_time
    heappush(queue,(time,start))

    while queue:
        if not queue: break
        
        time,cursor=heappop(queue)
        s=time%states
        map=map_states[s]

        if (s,cursor) not in visit: 
            visit.add((s,cursor))
            if cursor==dest: return time-start_time 
            for n in get_neighbor(cursor):
                nx,ny=n
                if 0<nx<max_row-1 and 0<ny<max_col-1 or (nx,ny) in [start,dest]:
                    if n not in map:
                        heappush(queue,(time+1,n))
    
t2=part2((max_row-1,max_col-2),(0,1),t1)
#print(t2)
t3=part2((0,1),(max_row-1,max_col-2),t1+t2)
#print(t3)

print(sum([t1,t2,t3]))

        
        
