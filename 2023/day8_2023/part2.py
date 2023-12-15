from collections import defaultdict, namedtuple 
from itertools import cycle
from math import lcm
import re

input=open('aoc8.txt').read()
instructions,node_input=input.split('\n\n')
l_r=namedtuple('l_r',['l','r'])
nodes=defaultdict(namedtuple)
all_A=list()


for line in node_input.split('\n'):
    node,l,r=re.findall(r'([A-Z0-9]{3})',line)
    nodes[node]=l_r(l,r)
    if node[-1]=='A': 
        all_A.append(node)

result=1

for a in all_A:
    to_visit=a
    step=0
    for idx,i in enumerate(cycle(instructions)):
        if to_visit[-1]=="Z":
            result=lcm(result,step)
            break
        to_visit=nodes[to_visit].l if i=="L" else nodes[to_visit].r
        step+=1
print(result)




        


