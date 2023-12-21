from collections import namedtuple

input=open('aoc16.txt').readlines()
matrix=[[l for l in line.strip()] for line in input]

w=len(matrix[0])
h=len(matrix)
nxt=namedtuple('nxt',["co","dir"])

#add next direction,co to the dictionary 
"""
    key: symbol in the map 
    R,L,U,D: on-going direction of beam
    nxt.co: coordinate to be added to current coordinates of beam
    nxt.dir: next direction of beam

"""


SYMBOL={
    ".":{"R": [nxt((0,1),"R")],"L":[nxt((0,-1),"L")],"U":[nxt((-1,0),"U")],"D":[nxt((1,0),"D")]},
    "/":{"R":[nxt((-1,0),"U")],"L":[nxt((1,0),"D")],"U":[nxt((0,1),"R")],"D":[nxt((0,-1),"L")]},
    "\\":{"R":[nxt((1,0),"D")],"L":[nxt((-1,0),"U")],"U":[nxt((0,-1),"L")],"D":[nxt((0,1),"R")]},
    "|": {"R":[nxt((-1,0),"U"),nxt((1,0),"D")],"L":[nxt((-1,0),"U"),nxt((1,0),"D")],"U":[nxt((-1,0),"U")],"D":[nxt((1,0),"D")]},
    "-":{"R":[nxt((0,1),"R")],"L":[nxt((0,-1),"L")],"U":[nxt((0,1),"R"),nxt((0,-1),"L")],"D":[nxt((0,1),"R"),nxt((0,-1),"L")]}

}

O={
    "R":(0,1), "L":(0,-1),"U":(-1,0),"D":(1,0)
}


v=set() #visited
e=set() # energized tiles 
start=nxt((0,0),"R")
active_nodes=list()
active_nodes.append(start)

while active_nodes:
    curr_beam=active_nodes.pop()
    # print(curr_beam)
    cur_co,cur_dir=curr_beam.co,curr_beam.dir #get curr coordinate, current direction of beam
    if curr_beam in v:
        continue
    else: 
        v.add(curr_beam) #add coordinate to a set
        e.add(cur_co)

        s=matrix[cur_co[0]][cur_co[1]] #get symbol from input
        next=SYMBOL[s][cur_dir] #get coordinate,dir from the dict to get to next tile 
        for n in next:
            nxt_co= tuple([sum([s,addx]) for s,addx in zip(cur_co,n.co)])
            if 0<=nxt_co[0]<w and 0<=nxt_co[1]<h: active_nodes.append(nxt(nxt_co,n.dir))
    

print(len(e))









