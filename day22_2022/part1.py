import math 
from itertools import groupby
from collections import defaultdict

global maze,max_height,max_width

#build a matrix contains all the symbol inputs
def parse(input):
    with open(input) as f:
        map,instructions=f.read().split('\n\n')
        max_width=max(len(line) for line in map.splitlines())
        max_height=len(map.splitlines())
        instructions.strip()
        instructions=["".join(instructions) \
                    for key,instructions in groupby(instructions, key=lambda c: c.isdigit())]
    return max_height,max_width,map,instructions

def build_maze(max_height,max_width,map):
    maze=defaultdict(list)
    for row,line in enumerate(map.splitlines()):
        maze[row]=[" " for _ in range(max_width)]
        for order,symbol in enumerate(line):
            maze[row][order]=symbol
    return maze

max_height,max_width,map,instructions=parse("aoc22.txt")
maze=build_maze(max_height,max_width,map)
class Coordinate:
    directions=["N","E","S","W"] #east, north, west, south
    #order 0,1,2,3 corresponds to north,east,south,west 
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.order=1
    def get_tile(self):
        if self.x<max_height and self.y<max_width:
            match maze[self.x][self.y]:
                case ".":
                    return "dot"
                case "#":
                    return "block"
                case _:
                    return "mty"
        else:
            return "mty"
    def move(self,direction):
        match direction:
            case "N":
                self.order=0
                return (self.x-1)%max_height,self.y%max_width
            case "E":
                self.order=1
                return self.x%max_height,(self.y+1)%max_width
            case "S":
                self.order=2
                return (self.x+1)%max_height,self.y%max_width
            case "W":
                self.order=3
                return self.x%max_height,(self.y-1)%max_width
            
    def turn(self,input):
        if input=="R":
            self.order+=1    
        else: 
            self.order-=1
        return self.directions[self.order%4] 

    def score(self,x,y,face):
        score=1000*(x+1)+4*(y+1)
        match face:
            case "E":
                return score
            case "S":
                return score+1 
            case "W":
                return score+2
            case "N":
                return score+3
    
    def wrap(self):
        cube_col=math.floor(self.y/50)
        cube_row=math.floor(self.x/50)
        # cube_row, cube_col, dir_order -> new_cube_row, new_cube_col, new_dir_order 
        mapping={
            (0,1,0):(3,0,1),
            (0,1,3):(2,0,1),
            (0,2,0):(3,0,0),
            (0,2,1):(2,1,3),
            (0,2,2):(1,1,3),
            (1,1,1):(0,2,0),
            (1,1,3):(2,0,2),
            (2,0,0):(1,1,1),
            (2,0,3):(0,1,1),
            (2,1,1):(0,2,3),
            (2,1,2):(3,0,3),
            (3,0,1):(2,1,0),
            (3,0,2):(0,2,2),
            (3,0,3):(0,1,2)
        }
        #inside the cube, cube_y is col indexes, cube_x is row indexes 
        in_cube_x=self.x%50
        in_cube_y=self.y%50
        #map to a new face 
        new_cube_row,new_cube_col,new_dir_order=mapping[(cube_row,cube_col,self.order)]
        
        # find off set when move left or down. 
        match self.order:
            case 0: #North: move up 
                off_set=in_cube_y
            case 1: # East: move right
                off_set=in_cube_x
            case 2: #South: move down
                off_set=49-in_cube_y
            case 3: #West: move left
                off_set=49-in_cube_x
        
        #find new x,y in cube after the mapping 
        match new_dir_order:
            case 0: #North: move up 
                new_in_cube_x=49
                new_in_cube_y=off_set

            case 1: # East: move right
                new_in_cube_x=off_set
                new_in_cube_y=0
            case 2: #South: move down
                new_in_cube_x=0
                new_in_cube_y=49-off_set
            case 3: #West: move left
                new_in_cube_x=49-off_set
                new_in_cube_y=49
        
        # set to new coordinate
        self.x=50*new_cube_row + new_in_cube_x
        self.y=50*new_cube_col + new_in_cube_y
        self.order=new_dir_order

        return self.x,self.y,self.order 

def solve():
    cursor=Coordinate(0,maze[0].index("."))
    face="E"
    
    for i in instructions: 
        
        if not i.isdigit():
            face=cursor.turn(i)
        
        else: 
            steps=int(i)

            for step in range(steps):
                prev_x,prev_y=cursor.x,cursor.y
                cursor.x,cursor.y=cursor.move(face)

                if cursor.get_tile()=='block' :
                    cursor.x,cursor.y=prev_x,prev_y
                    break
                #if empty, go back in opposite direction
                elif cursor.get_tile()=="mty":
                    oppo_dir=(cursor.directions.index(face)+2)%4
                    cursor.x,cursor.y=prev_x,prev_y
                    while maze[cursor.x][cursor.y]!=' ':
                        cursor.x,cursor.y=cursor.move(cursor.directions[oppo_dir])
                    cursor.x,cursor.y=cursor.move(face)
                    if maze[cursor.x][cursor.y]=="#":
                        cursor.x,cursor.y=prev_x,prev_y
                        break
                    else:
                        continue
                else:
                    continue
    
    return cursor.score(cursor.x,cursor.y,face)


if __name__=="__main__":
 
    print(solve())