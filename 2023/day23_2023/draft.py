def flatten(sequence):
    """flatten a multi level list or something
    >>> list(flatten([1, [2], 3]))
    [1, 2, 3]
    >>> list(flatten([1, [2], [3, [4]]]))
    [1, 2, 3, 4]
    """
    for element in sequence:
        if hasattr(element, '__iter__'):
            yield from flatten(element)
        else:
            yield element





# r=[]
# v=set()
# q=[]
# q.append((0,s))
# while q:
#     steps,(x,y)=q.pop(-1)
#     print(f'step {steps} at {(x,y)}')
#     if (x,y)==e: break
#     if (steps,(x,y)) in v: continue
        
#     v.add((steps,(x,y)))
#     steps+=1 

#     if slopes(x,y):
#         match input[x][y]:
#             case "^":
#                 dx,dy=ADJ["n"]
#             case "v":
#                 dx,dy=ADJ["s"]
#             case "<":
#                 dx,dy=ADJ["w"]
#             case ">":
#                 dx,dy=ADJ['e']
#         q.append((steps,(x+dx,y+dy)))

#     else: 
#         for nb in ADJ:
#             dx,dy=ADJ[nb]
#             nx,ny=x+dx,y+dy
            
#             if limit(nx,ny) and not forest(nx,ny):
#                 q.append((steps,(nx,ny)))





a=2
b=2
print(a,b in range(3))