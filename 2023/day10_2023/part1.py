from queue import Queue 

input=open('aoc10.txt').readlines()
matrix=[i.strip() for i in input]

""" node is at center of the coordinate, 
each elem represents where the symbol might connect to"""
symbol={
        "|": [ ( 0,-1), ( 0, 1) ],
        "-": [ (-1, 0), ( 1, 0) ],
        "L": [ ( 0,-1), ( 1, 0) ],
        "J": [ ( 0,-1), (-1, 0) ],
        "7": [ (-1, 0), ( 0, 1) ],
        "F": [ ( 1, 0), ( 0, 1) ],
    }

""" find s """
for y,r in enumerate(matrix):
    for x,c in enumerate(r):
        if c=="S": 
            sx,sy=x,y

            break

    
""" find s's immediate neighbors"""       
q=Queue()
#check for linked neighbors
for nx,ny in [(-1,0),(1,0),(0,-1),(0,1)]:
    shape=matrix[sy+ny][sx+nx]
    if shape in symbol:
        for dx,dy in symbol[shape]:
            if sy==sy+ny+dy and sx==sx+nx+dx: 
               
                q.put((1,(sx+nx,sy+ny)))

#bfs for max distance 
dist={(sx,sy):0}
while q:
    if q.empty(): break
    d,(x,y)=q.get()
    # print(f'getting {(y,x)}')
    if (x,y) in dist: continue
    dist[(x,y)]=d

    for dx,dy in symbol[matrix[y][x]]:
        # print(f'distance: {d+1}\n co: {(y+dy,x+dx)}')
        # for each neighbor node,extend the coordinate to their neighbor based on their shape 
        q.put((d+1,(x+dx,y+dy)))




# if __name__=="__main__":

#     print(max(dist.values()))







    

    
