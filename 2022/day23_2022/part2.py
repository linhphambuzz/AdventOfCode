from collections import Counter
with open('input.txt') as f:
    elves=[(x,y) for x,line in enumerate(f) for y,char in enumerate(line) if char=='#']
             
    
def neighbors(coordinate):
    x,y=coordinate
    off_set=[(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    for o in off_set:
        yield (x+o[0],y+o[1])

def area_clear(orientation:str,co:set,elf_dict:dict)->bool:
    x,y=co
    match orientation: 
        case 'N':
            slots=[(x-1,y-1),(x-1,y),(x-1,y+1)]
        case 'S':
            slots=[(x+1,y-1),(x+1,y),(x+1,y+1)]
        case 'W':
            slots=[(x-1,y-1),(x,y-1),(x+1,y-1)]
        case 'E':
            slots=[(x-1,y+1),(x,y+1),(x+1,y+1)]

    if any([s in elf_dict for s in slots]): return False
    
    return True

   
MOVE={'N':(-1,0),'S':(1,0),'W':(0,-1),'E':(0,1)}

def solve(elves):
    priority=['N','S','W','E']
    elf_dict={e:e for e in elves}
    move=True 
    round=0
    while move:
        move=False
        round+=1
        print(f'round {round}')
        for elf in elf_dict:
            for n in neighbors(elf): #if there's a neighbor
                if n in elf_dict:
                    move=True

                    for p in priority:
                        if area_clear(p,elf,elf_dict):
                            dx,dy=MOVE[p]
                            elf_dict[elf]=(elf[0]+dx,elf[1]+dy)
                            break
                        else:
                            continue
                    break
        new_values=list(elf_dict.values())
        
        for elf,new_elf in elf_dict.items():
            if new_values.count(new_elf)>1:
                elf_dict[elf]=elf    
        elf_dict={e:e for e in elf_dict.values()}
        priority.append(priority.pop(0))
        #print(elf_dict)
        #if round==10: 
        #    final=elf_dict.keys()
        #    break
    #b,t=max(i[0] for i in final),min(i[0] for i in final)
    #r,l=max(i[1] for i in final),min(i[1] for i in final)
    #return (b-t+1)*(r-l+1)-len(final)
    return round

            
    

solve(elves)





                         
                    
                    






    

solve(elves)







