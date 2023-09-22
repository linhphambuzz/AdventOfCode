from collections import defaultdict 
caves=defaultdict(set)
f=open("test.txt").read().split("\n")
for line in f:
    node1,node2=line.split('-')
    caves[node1].add(node2)
    caves[node2].add(node1)

Islower= lambda s: s[0].islower()
print(caves)
cnt=0
visit=set()
stacks=['start']
path=''
while stacks:
    to_visit=stacks.pop()
    path+=str(to_visit) + '->' 
    if to_visit=='end': cnt+=1;  
    if Islower(to_visit):visit.add(to_visit)
    for nb in caves[to_visit]:
        if nb not in visit:  stacks.append(nb)
print(path) 
       
    

