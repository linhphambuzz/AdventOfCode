from collections import defaultdict

input=open("aoc14.txt").readlines()
original=[[c for c in line.strip()]for line in input]
north=defaultdict(set)
west=defaultdict(set)
south=defaultdict(set)
east=defaultdict(set)


def replace_matrix(original,cycle,d):
    for l_idx,line in enumerate(original):
        for c_idx,c in enumerate(line):
            if original[l_idx][c_idx]=="O":
                if (l_idx,c_idx) not in d[cycle]: original[l_idx][c_idx]="."
            elif original[l_idx][c_idx]==".":
                if (l_idx,c_idx) in d[cycle]:original[l_idx][c_idx]="O"  
            else:
                continue

"""North"""

def move_N(matrix,cycle,d):
    w=len(matrix[0])
    m=[[line[idx] for line in matrix] for idx in range(w)]
    for l_idx,line in enumerate(m):
        hold_idx=0
        for c_idx, c in enumerate(line):
            if c=="#":
                hold_idx=c_idx+1
            elif c=="O":
                d[cycle].add(tuple([hold_idx,l_idx]))
                hold_idx+=1
            else:
                continue
    #change the original matrix
    replace_matrix(matrix,cycle,d)
    return matrix

""" west"""

def move_W(matrix,cycle,d):
    for l_idx,line in enumerate(matrix):
        hold_idx=0
        for c_idx, c in enumerate(line):
            if c=="#":
                hold_idx=c_idx+1
            elif c=="O":
                d[cycle].add(tuple([l_idx,hold_idx]))
                hold_idx+=1
            else:
                continue
    replace_matrix(matrix,cycle,d)

    return matrix 

"""south"""
def move_S(matrix,cycle,d):
    w=len(matrix[0])
    m=[[line[idx] for line in matrix] for idx in range(w)]
    
    for l_idx,line in enumerate(m):
        hold_idx=0
        for c_idx, c in enumerate(line[::-1]):
            if c=="#":
                hold_idx=c_idx+1
            elif c=="O":
                d[cycle].add(tuple([len(m[0])-1-hold_idx,l_idx]))
                hold_idx+=1
            else:
                continue
    replace_matrix(matrix,cycle,d)

    return matrix

"""east """

def move_E(matrix,cycle,d):
    for l_idx,line in enumerate(matrix):
        hold_idx=0
        for c_idx, c in enumerate(line[::-1]):
            if c=="#":
                hold_idx=c_idx+1
            elif c=="O":
                d[cycle].add(tuple([l_idx,len(matrix[0])-1-hold_idx]))
                hold_idx+=1
            else:
                continue
    replace_matrix(matrix,cycle,d)
    return matrix

"""
the while loop is to find coordinate after tilting each cycle
the ultimate goal is to detect in how many cycles would there be a repeated pattern
if a repeated coordinate detected, exit the while loop
the coordinate for the required cycle is calculated as such:
    after "c" cycle, there will be a number of repeat loops that keep circling
    therefore, the coordinate of the required cycle is exactly of the remainder of:
            (required_cycle-c)%repeat_loop
"""


ORDER=[move_N,move_W,move_S,move_E]
d_order=[north,west,south,east]
cycle=0
repeat_loop=None
while True:
    cycle+=1    
    for move,d in zip(ORDER,d_order):
        original=move(original,cycle,d)
 
    for c in range(cycle)[1:]:
        if east[c]==east[cycle]:
            repeat_loop=cycle-c
            break
    if repeat_loop: break

def total_load(d,cycle):
    re=0
    h=len(original)
    for r,_ in d[cycle]:
        re+=(h-r)
    return re

# print(f'loop {repeat_loop}')
remainder=repeat_loop if (1000000000-c)%repeat_loop==0 else (1000000000-c)%repeat_loop
# print(f'c {c}')
# print(remainder)
load=total_load(east,c+remainder)
print(load)





