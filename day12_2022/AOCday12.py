from collections import defaultdict
import heapq as hp
class GRAPH:
    
    def __init__(self,file):
        self.file=file
        self.lmatrix=list(list()) #letter matrix 
        self.nmatrix=list(list()) #node matrix 
        self.graph=defaultdict(list)
        self.Sp=0
        self.Ep=0
        self.MAX_STEP=10e7
        self.EDGE=1
        self.node=None
        with open(self.file) as f:
            lines=f.read().split('\n')
            self.number_rows=len(lines) 
            self.number_cols=len(lines[0].strip())
            self.lmatrix=[[" " for _ in range(self.number_cols)] for _ in range(self.number_rows)] 
            self.nmatrix=[[" " for _ in range(self.number_cols)] for _ in range(self.number_rows)]
            for row,line in enumerate(lines):
                line.strip()
                for col,letter in enumerate(line):
                    self.nmatrix[row][col]=col+self.number_cols*row #node matrix fill with number from 1 to N 
                    if letter=="S":
                        self.Sp=self.nmatrix[row][col]
                        letter="a"
                    if letter=="E":
                        self.Ep=self.nmatrix[row][col]
                        letter="z"
                    self.lmatrix[row][col]=letter #letter matrix filled with all letters 
                    


    def build_graph(self):
        for r in range(self.number_rows):
            for c in range(self.number_cols):
                neighbors=self.check_neighbor(r,c)
                self.graph.update({self.nmatrix[r][c]:neighbors})
        return self.graph
#given coordinate of a node, return list of adj. neighbor 
    def check_neighbor(self,row,column): 
        nb=[]
        node=ord(self.lmatrix[row][column]) 
        lnode=ord(self.lmatrix[row][column-1]) if column-1!=-1 else None
        rnode=ord(self.lmatrix[row][column+1]) if column+1<self.number_cols else None
        tnode=ord(self.lmatrix[row-1][column])  if row-1!=-1 else None
        bnode=ord(self.lmatrix[row+1][column])if row+1<self.number_rows else None
        if self.check_nodes(tnode,node):
            nb.append(self.nmatrix[row-1][column])
        if self.check_nodes(lnode,node):
            nb.append(self.nmatrix[row][column-1])
        if self.check_nodes(rnode,node):
            nb.append(self.nmatrix[row][column+1])
        if self.check_nodes(bnode,node):
            nb.append(self.nmatrix[row+1][column])
        return nb
    #check to see if 2 adj. node can be moved between each other    
    def check_nodes(self,num1,num2): #neighbor node can only be equal or 1 bigger 
        if num1!=None and num2!=None and  num1-num2<=1:
            return True 
        else: 
            return False
    

    def find_a(self):
        all_a=list()
        for r,line in enumerate(self.lmatrix):
            for l,letter in enumerate(line):
                if letter=="a":
                    all_a.append(self.nmatrix[r][l])
        return all_a 

#visit the unvisit node with smallest distance from source node 
#helper for dijkstra 
    def node_to_visit(self,visited,steps):
        min=self.MAX_STEP
        for vnode,distance in enumerate(steps):
            if distance<min and visited[vnode]==False:
                min=distance
                self.node=vnode
        return self.node 

#dijkstra using list only, with helper above 
    def dijkstra(self,starting_node,end_node):
        visited=[False for _ in range(self.number_cols*self.number_rows)] 
        #previous=[" " for _ in range(self.number_cols*self.number_rows) ]
        steps=[self.MAX_STEP for _ in range(self.number_cols*self.number_rows)] #distance from source
        steps[starting_node]=0 # is source node
        for i in range(self.number_cols*self.number_rows):
            self.node= self.node_to_visit(visited,steps)
            visited[self.node]=True #mark node as visited
            if self.node==end_node: 
                return steps[end_node]       
            else:
                for neighbor in self.graph[self.node]:
                    if not visited[neighbor]:
                        new_steps=steps[self.node]+ self.EDGE
                        if new_steps<steps[neighbor]:
                            steps[neighbor]=new_steps
                        #previous[neighbor]=node
 
        return steps[end_node]
#diskstra using priority heap 
    def dijstra2(self,starting_node,end_node):
        visited=set()
        pq=[]
        hp.heappush(pq,(0,starting_node))
        while pq:
           steps,node=hp.heappop(pq)
           if node not in visited:
            visited.add(node)
            if node==end_node:
                return steps
            for neighbor in self.graph[node]:
                hp.heappush(pq,(steps+self.EDGE,neighbor))
        
def part1(file): 
    graph=GRAPH(file)
    graph.build_graph() #build the graph 
    return graph.dijkstra(graph.Sp,graph.Ep)

def part2(file):
    graph=GRAPH(file)
    min=graph.MAX_STEP
    graph.build_graph()
    for a in graph.find_a():
        if graph.dijstra2(a,graph.Ep)!=None:
            dist=graph.dijstra2(a,graph.Ep)
            min=dist if dist<min else min
    return min 

if __name__=="__main__":

    print(part1('aoc12.txt'))
    print(part2('aoc12.txt'))