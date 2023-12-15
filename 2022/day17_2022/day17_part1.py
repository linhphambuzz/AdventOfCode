'''
chamber is 7 units wide
left edge is 2 units away from rocks
bottom edge is 3 units above the highest rock
rock alternates between being pushed by a jet, and then falling one unit down
'''
from itertools import cycle
from collections import defaultdict
input=open('test.txt').read().strip()
#define shape given top rock
def get_rock(number,top_rock):
    match number:
        case 0:#minus 
            return set([(2,top_rock+4),(3,top_rock+4),(4,top_rock+4),(5,top_rock+4)])
        case 1: #plus 
            return set([(2,top_rock+5),(3,top_rock+4),(3,top_rock+5),(4,top_rock+5),(3,top_rock+6)])
        case 2:# L shape 
            return set([(2,top_rock+4),(3,top_rock+4),(4,top_rock+4),(4,top_rock+5),(4,top_rock+6)])
        case 3: #vertical
            return set([(2,top_rock+4+i) for i in range(4)])
        case 4: #square 
            return set([(2,top_rock+4),(3,top_rock+4),(2,top_rock+5),(3,top_rock+5)])

def move_left(shape):
    shape=set([(i-1,j) for i,j in shape])
    return shape
    
def move_right(shape):
    shape=set([(i+1,j) for i,j in shape])
    return shape

def move_down(shape):
    shape=set([(i,j-1) for i,j in shape])
    return shape

def move_up(shape):
    shape=set([(i,j+1) for i,j in shape])
    return shape

def is_out_range(shape): 
    if any([(i[0]<0 or i[0]>6) for i in shape]): return True
    return False 

def is_collided(puzzle:set,new:list)->bool:
    for n in new:
        if n in puzzle: return True
    return False


puzzle=set()
for c in [[i,0] for i in range(7)]:
    puzzle.add(tuple(c))  #the chamber's base 

pushed=cycle(input)
shape=cycle([i for i in range(5)]) #o is hor. bar, 1 is plus, 2 is L, 3 is ver. bar, 4 is square
top_rock=0
for rocks,s in enumerate(shape):
    #bottom of cur. rock vs top of settled rocks
    if rocks== 2022: 
        final=new
        break #after 3 rocks have fallen 
    new=get_rock(s,top_rock) 
    while True: 
        p=next(pushed)
        if p=="<":
            new=move_left(new)
            #print(f'after left move{new} of shape no.{s}')
            if is_out_range(new) or is_collided(puzzle,new): 
                #print("out of range,moving right..")
                new=move_right(new)
            new=move_down(new)
            #print(f'after move down {new} of shape no.{s}')
            if is_collided(puzzle,new):
                #print("collided, moving up")
                new=move_up(new)
                #print(f"final pos {new}")
                for n in new:
                    top_rock=max(top_rock,n[1])
                break
        else:
            new=move_right(new)
            #print(f'after right move{new} of shape no.{s}')
            if is_out_range(new) or is_collided(puzzle,new):
                #print("out of range,moving left..")
                new=move_left(new) #go back 
            new=move_down(new) 
            #print(f'after down move{new} of shape no.{0}')
            if is_collided(puzzle,new):
                #print("collided, moving up")
                new=move_up(new)
                #print(f'final pos {new}')
                for n in new:
                    top_rock=max(top_rock,n[1])
                    puzzle.add(tuple(n))
                break

print(max(i[1] for i in final))
                
            











    
    
    





    







