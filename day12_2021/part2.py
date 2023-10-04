from part1 import caves, Islower 
ppath=[]
cnt=0 

#check if there's any lower node already visited twice 
twice_detected=lambda path: any(path.count(node)==2 for node in path if Islower(node))

def dfs2(visited,node,path):
    if all(nb in visited for nb in caves[node]) or node=='end': 
        path.append(node)
        ppath.append(path)
    
    elif not Islower(node): 
        path.append(node) 
        for nb in caves[node]:
            dfs2(visited.copy(),nb,path[:])
    
    elif Islower(node) and node not in visited:
        if node=='start': path.append(node) ; visited.add(node)
        elif not twice_detected(path):
            path.append(node)
            if path.count(node)==2: 
                visited.add(node)
                for lower_node in path:
                    if Islower(lower_node):visited.add(lower_node)
        else:
            if node not in path:
                path.append(node)
                visited.add(node)
        for nb in caves[node]:
            dfs2(visited.copy(),nb,path[:])




dfs2(set(),'start',[])

for p in ppath:
    if p[-1]=='end':
        cnt+=1
        print(p)
print(cnt)