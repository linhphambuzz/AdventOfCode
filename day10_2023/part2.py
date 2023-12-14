from part1 import dist,matrix,symbol,sx,sy


""" replacing S with its actual shape"""
shape={s for s in symbol}
for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
    if (sx+dx,sy+dy) in dist: 
        match (dx,dy):
            case (0,-1):   
                if matrix[sy+dy][sx+dx] in "7F|":
                    shape&={"L","|","J"}
            case (0,1):
                if matrix[sy+dy][sx+dx] in "LJ|":
                    shape&={"7","F","|"}
            case (-1,0):
                if matrix[sy+dy][sx+dx] in "LF-":
                    shape&={"-","7","J"}
            case (1,0):
                if matrix[sy+dy][sx+dx] in "-7J":
                    shape&={"L","F","-"}

# print(shape)
(s,)=shape
matrix=[r.replace("S",s) for r in matrix]



""" get dimensions of matrix"""
max_w,max_h=len(matrix[0]),len(matrix)

cnt=0
"""
if there's a ray shooting from a point and it crosses odd numbers of edges , it's inside the polygon 
if it crossed even numbers of edge it's outside
"""
for y, line in enumerate(matrix):
    for x,s in enumerate(line):
        #if belong to the loop, skip
        if (x,y) in dist: continue
        #count the cross if a ray to be shooted from the point 
        cross=0  
        xx,yy=x,y

        while xx<max_w and yy<max_h:
            p=matrix[yy][xx]
            if (xx,yy) in dist and p!="7" and p!="L":
                cross+=1
            xx+=1
            yy+=1
            
        if cross%2==1: 
            
            cnt+=1

print(f'cnt {cnt}')


        






