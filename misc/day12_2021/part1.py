from collections import defaultdict 
caves=defaultdict(set)
f=open("test2.txt").read().split("\n")
for line in f:
    node1,node2=line.split('-')
    caves[node1].add(node2)
    caves[node2].add(node1)

Islower= lambda s: s[0].islower()

cnt=0
ppath=[]

def dfs(visited,node,path):
    if all(nb in visited for nb in caves[node]) or node=='end': 
        path.append(node)
        ppath.append(path)
    elif node not in path or (node in path and not Islower(node)):
        path.append(node)   
        if Islower(node): visited.add(node)
        for nb in caves[node]:
            dfs(visited.copy(),nb,path[:])


if __name__=="__main__":     
    dfs(set(),'start',[])       
    for p in ppath:
        if p[-1]=='end':
            print(p)
            cnt+=1
    print(cnt)

