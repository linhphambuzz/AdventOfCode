from part1 import Coordinate,parse,build_maze

def solve():
    max_height,max_width,map,instructions=parse("aoc22.txt")
    maze=build_maze(max_height,max_width,map) 

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
                
                #start wrapping when go towards the edge 
                elif cursor.get_tile()=="mty":
                    cursor.x,cursor.y=prev_x,prev_y
                    prev_order=cursor.order
                    cursor.x,cursor.y,cursor.order=cursor.wrap()
                    face=cursor.directions[cursor.order]
                    
                    if cursor.get_tile()=="block":
                        cursor.x,cursor.y=prev_x,prev_y
                        cursor.order=prev_order
                        break
                
                else:
                    continue

    return cursor.score(cursor.x,cursor.y,cursor.directions[cursor.order])

if __name__=="__main__":
    print(solve())

            
