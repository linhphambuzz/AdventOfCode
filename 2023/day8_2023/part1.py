from collections import defaultdict, namedtuple 
from itertools import cycle
import re

input=open('aoc8.txt').read()
instructions,node_input=input.split('\n\n')
l_r=namedtuple('l_r',['l','r'])
nodes=defaultdict(namedtuple)
start,end='AAA','ZZZ'
step=0 

for line in node_input.split('\n'):
    node,l,r=re.findall(r'[A-Z]{3}',line)
    nodes[node]=l_r(l,r)

to_visit=start
for i in cycle(instructions):
    if to_visit==end: 
        break
    else: 
        step+=1
        to_visit=nodes[to_visit].l if i=='L' else nodes[to_visit].r

print(step)


    