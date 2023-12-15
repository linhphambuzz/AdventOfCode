from heapq import heappush,heappop

input=open('aoc11.txt').readlines()
matrix= [[l for l in line.strip()] for line in input]
w,h=len(matrix[0]),len(matrix)

""" expand the matrix"""

def insert_blank(map,idx):
    first=map[:idx]
    secnd=map[idx:]
    blank=[["."]*len(map[0])]
    map=first+blank+secnd
    return map

blank_r=list()
blank_c=list()
for r_idx,r in enumerate(matrix):
    if all(char=='.' for char in r): blank_r.append(r_idx)

for idx,bl in enumerate(blank_r):
    matrix=insert_blank(matrix,bl+idx) 

#rotate the matrix, to insert blank column
rot_matrix=[[r[idx] for r in matrix] for idx in range(len(matrix[0]))]
for r_idx,r in enumerate(rot_matrix):
    if all(char=='.' for char in r): blank_c.append(r_idx)
for idx,bl in enumerate(blank_c):
    rot_matrix=insert_blank(rot_matrix,bl+idx) 

#rotate back 
matrix=[[r[idx] for r in rot_matrix] for idx in range(len(rot_matrix[0]))]

""" find all # node """
nodes=list()
for y,line in enumerate(matrix):
    for x,c in enumerate(line):
        if c=="#": 
             nodes.append((y,x))
            

total_dist=0 

for node_idx,node in enumerate(nodes):
    for other_node in nodes[:node_idx]:
        for r in range(min([node[0],other_node[0]]),max([node[0],other_node[0]])):
            total_dist+=1 
        for c in range(min([node[1],other_node[1]]),max([node[1],other_node[1]])):
            total_dist+=1 

print(total_dist)








