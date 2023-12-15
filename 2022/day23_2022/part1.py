from collections import Counter
with open('input.txt') as f:
    elves=[(x,y) for x,line in enumerate(f) for y,char in enumerate(line) if char=='#']
input=[line.strip() for line in open('input.txt').readlines()]
height=len(input)
width=len(input[0])

def get_neighbor(orientation:str,coordinate:set,elves:list)->tuple:
    x,y=coordinate
    set_elves=set(elves)
    match orientation:
        case 'N':
            if all([item not in set_elves for item in [(x-1,y+i) for i in [-1,0,1]]]):
                return (x-1,y)
                
        case 'S':
            if all([item not in set_elves for item in [(x+1,y+i) for i in [-1,0,1]]]):
                return (x+1,y)
            
        case 'W':
            if all([item not in set_elves for item in [(x+i,y-1) for i in [-1,0,1]]]):
                return (x,y-1)
        case 'E':
            if all([item not in set_elves for item in [(x+i,y+1) for i in [-1,0,1]]]):
                return (x,y+1)
        


def surrounded(coordinate:set,elves:set)->bool:
    x,y=coordinate
    upper=[(x-1,y-1),(x-1,y),(x-1,y+1)]
    side=[(x,y-1),(x,y+1)]
    lower=[(x+1,y-1),(x+1,y),(x+1,y+1)]
    if any([slot in elves for slot in upper+side+lower]): return True
    return False
        
priority=['N','S','W','E']
#rounds=1
#print(f' round {rounds}')

def solve(rounds)->int:
    for move in range(rounds):
        print(f'move {move}')
        new_elves=[None] * len(elves)
        for indx,elf in enumerate(elves):
            p=0
            while p<4:
                if not surrounded(elf,set(elves)): 
                    nb=elf
                else:
                    nb=get_neighbor(priority[p],elf,set(elves))
                if not nb:
                    p+=1
                else:
                    break
            new_elves[indx]=nb if nb!=None else elf
        count=Counter(new_elves)
        for indx,new_elf in enumerate(new_elves):
            if count[new_elf]==1: 
                elves[indx]=new_elf
        
        priority.append(priority.pop(0))

        #if part2 and not any([surrounded(e,elves) for e in elves]): return move+2
    
    
    return elves
    


def count_slots(elves):
    l=min([elf[1] for elf in elves])
    r=max([elf[1] for elf in elves])
    u=min([elf[0] for elf in elves])
    b=max([elf[0] for elf in elves])
    return (r-l+1)*(b-u+1)-len(elves)

#part 1
print(count_slots(solve(10)))






#helper
def render(co_list:list)->None:
    h=height
    w=width
    r=[["." for _ in range(width)] for _ in range(height)]
    for co in co_list:
        x,y=co
        r[x][y]="#"
    for rr in r:
        print(f'{"".join(rr)}')

#render(new_elves)

    




    
    
    
    


        


        
        


        









    
