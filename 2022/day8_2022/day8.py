input=open("test.txt").read().split('\n')
rows=len(input)
cols=len(input[0])
matrix= [[" "for _ in range(cols)] for _ in range(rows)]
visible_edges=2*(cols+rows)-4
#create matrix from input numbers 
for row_number,row in enumerate(input):
    for column_number,number in enumerate(row): 
        matrix[row_number][column_number]=int(number)

'''
Helpers function to see if a tree is visible from a certain angle for part 1 
'''
def is_visible_from_left(x,y,matrix): #x,y is position of node 
    for y0 in range(y):
        if matrix[x][y0]>=matrix[x][y]:
            return False
    return True

def is_visible_from_right(x,y,matrix,columns): 
    for y0 in range(y+1,columns):
        if matrix[x][y0]>=matrix[x][y]:
            return False
    return True

def is_visible_from_top(x,y,matrix):
    for x0 in range(x):
        if matrix[x0][y]>=matrix[x][y]:
            return False 
    return True

def is_visible_from_bottom(x,y,matrix,rows):
    for x0 in range(x+1,rows):
        if matrix[x0][y]>=matrix[x][y]:
            return False 
    return True

'''
Helper functions for part 2 
'''
def from_left(x,y,matrix): #x,y is position of node 
    count=0
    for y0 in range(y-1,-1,-1):
        if matrix[x][y0]<matrix[x][y]:
            count+=1
        else:
            count+=1   #if there's a taller/same height tree
            break
    return count

def from_right(x,y,matrix,columns): 
    count=0
    for y0 in range(y+1,columns):
        if matrix[x][y0]<matrix[x][y]:
            count+=1
        else:
            count+=1   #if there's a taller/same height tree
            break
    return count

def from_top(x,y,matrix):
    count=0
    for x0 in range(x-1,-1,-1):
        if matrix[x0][y]<matrix[x][y]:
            count+=1
        else:
            count+=1   #if there's a taller/same height tree
            break
    return count

def from_bottom(x,y,matrix,rows): 
    count=0
    for x0 in range(x+1,rows):
        if matrix[x0][y]<matrix[x][y]:
            count+=1
        else:
            count+=1   #if there's a taller/same height tree
            break
    return count

#solve 
def part1(): 
    count=visible_edges
    for i in range(1,rows-1):
        for j in range(1,cols-1):
            if is_visible_from_top(i,j,matrix)==True \
            or is_visible_from_bottom(i,j,matrix,rows)==True \
            or is_visible_from_left(i,j,matrix)==True \
            or is_visible_from_right(i,j,matrix,cols)==True:
                count+=1
    return count

def part2():
    max_score=1
    for i in range(1,rows):
        for j in range(1,cols):
            left=from_left(i,j,matrix)
            right=from_right(i,j,matrix,cols)
            top=from_top(i,j,matrix)
            bottom=from_bottom(i,j,matrix,rows)
            score=left*right*bottom*top
            if score > max_score:
                max_score=score
    return max_score


if __name__=="__main__":
    print(f'part 1: {part1()} \
            part 2: {part2()}')





