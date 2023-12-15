from collections import defaultdict,deque

from part1 import find_value,values

"""
find 'humn' value so that 2 nodes in root operation are equal'
"""
#read input
input=open("aoc21.txt").readlines()
monkey_operation=defaultdict(list)
values=defaultdict(list)
operation=defaultdict(str)
for line in input:
    name=line[:line.index(":")]
    oper=(line[line.index(":")+1:]).strip()
    if len(oper.split())==1:
        monkey_operation[name]=values[name]=int(oper)
    else:
        monkey_operation[name]=oper.split()

#build tree with node only contains the operations
def build_tree(monkey_operation):
    tree=defaultdict(list)
    for node in monkey_operation:
        if type(mk:=monkey_operation[node])!=int:
            tree[node]=[mk[0],mk[2]]
    return tree

#helper to check branch contains node "humn"
def branch_include_humn(node):
    xpanded_tree=bfs(tree,node)
    if 'humn' in xpanded_tree: return True
    return False

def bfs(tree,node):
    s=deque()
    ll=list()
    s.append(node)
    while s:
        n=s.popleft()
        ll.append(n)
        if not tree[n]: continue
        for nn in tree[n]:
            s.append(nn)
    return ll

def solve():
    for matching_node in tree['root']:
        if not branch_include_humn(matching_node):
            node_wo_humn=find_value(matching_node)
        else:
            node_w_humn=matching_node
#print(K,parent_node)
    def get_humn(node_w_humn,node_wo_humn):
        pass_value=node_wo_humn
        while True:
            lnode,o,rnode=monkey_operation[node_w_humn]
            node_to_go=lnode if branch_include_humn(lnode) else rnode
            known_node=lnode if node_to_go!=lnode else rnode
            known_value=find_value(known_node) 
            if o=="+":
                r=pass_value-known_value 
            elif o=="-" and known_node==rnode:
                r=pass_value+known_value
            elif o=="-" and known_node==lnode:
                r= known_value-pass_value
            elif o=="*":
                r=pass_value/known_value
            elif o=="/" and known_node==rnode:
                r=pass_value*known_value
            else:
                r=known_value/pass_value
            node_w_humn=node_to_go
            pass_value=r
            if node_to_go=="humn":
                #print(known_node) 
                return r
    return get_humn(node_w_humn,node_wo_humn)

if __name__=="__main__":
    tree=build_tree(monkey_operation)
    print(solve())
    