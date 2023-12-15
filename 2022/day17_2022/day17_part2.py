from collections import namedtuple,defaultdict
from itertools import cycle,count

def parseInput(file):
    input=[]
    f=open(file).read().strip()
    push=namedtuple('push',['indx','dir']) #direction is L/R 
    for indx,dir in enumerate(f):
        input.append(push(indx,dir))
    return input 


def moveable(o,rock,dir): 
    collided= lambda rock: any(r+DIR[dir]+o in puzzle for r in rock)
    if all(-1<(o+r+DIR[dir]).real<7 and (o+r+DIR[dir]).imag>0  for r in rock) \
    and not collided(rock): return True 
    return False 





puzzle=set()
ROCKS=[(0,1,2,3),(1,1j,1+1j,2+1j,1+2j),(0,1,2,2+1j,2+2j),(0,1j,2j,3j),(0,1,1j,1+1j)]
rock=namedtuple('rock','indx pts')
ROCKS=cycle([rock(indx,pts) for indx,pts in enumerate(ROCKS)]) #pts is points 
pushed=cycle(parseInput("aoc17.txt"))
DIR={'<':-1,'>':1,'v':-1j}
rock_cnt,top,height_cycle=0,0,0
d=defaultdict(tuple)



for rock_no in count(1):
    if rock_cnt==1000000000000: 
        print(int(top+height_cycle))
        #print(puzzle)
        break
    r_idx,r=next(ROCKS)
    rock_cnt+=1
    o=complex(2,top+4) #start position of rock, main coordinate to be shifted around 

    while True: 
        p_idx,dir=next(pushed)
        if moveable(o,r,dir): 
            o+=DIR[dir] #move L/R
            #print(f'move side {o}')
        if moveable(o,r,'v'):
            o+=DIR['v'] #move down
            #print(f'move down {o}')
        else: break 
    
    for rr in r:
        puzzle.add(rr+o) #add rock to puzlle 

    top=max(top,o.imag+[0,2,2,3,1][r_idx]) #hard coded the top of each shape

#detecting repeating pattern based off rock indx and push indx
    key=r_idx,p_idx
    if key in d and rock_cnt>2000 and height_cycle==0:
        print(key) 
        prev_rcnt,prev_top=d[key]
        rem_cycles,remainder=divmod(1000000000000-rock_cnt,rock_cnt-prev_rcnt)
        height_cycle=(top-prev_top)*rem_cycles
        rock_cnt+=rem_cycles*(rock_cnt-prev_rcnt)
    else: 
        d[key]=(rock_cnt,top)




    
    










    

    

    



        

        