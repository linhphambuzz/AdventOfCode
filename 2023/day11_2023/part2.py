input=open('aoc11.txt').readlines()
matrix= [[l for l in line.strip()] for line in input]

blank_r,blank_c=list(),list()

for r_idx,r in enumerate(matrix):
    if all(char=='.' for char in r): blank_r.append(r_idx)

for c_idx,c in enumerate([[line[idx] for  line in matrix] for idx in range(len(matrix))]):
    if all(char=='.' for char in c): blank_c.append(c_idx)

""" find all nodes """
nodes=list()
for y,line in enumerate(matrix):
    for x,c in enumerate(line):
        if c=="#": 
             nodes.append((y,x))

total_dist=0 

for node_idx,node in enumerate(nodes):
    for other_node in nodes[:node_idx]:
        for r in range(min([node[0],other_node[0]]),max([node[0],other_node[0]])):
            total_dist+=1 if r not in blank_r else 1000000
        for c in range(min([node[1],other_node[1]]),max([node[1],other_node[1]])):
            total_dist+=1 if c not in blank_c else 1000000

print(total_dist)

