
'''
helper function to return row of the image that 
the CRT pixel belong to  
'''
def get_row(cycle):
    match  cycle:
            case i if 1<=i<41: 
                row=0
            case i if 41<=i<81:
                row=1
            case i if 81<=i<121:
                row=2
            case i if 121<=i<161:
                row=3
            case i if 161<=i<201:
                row=4
            case i if 201<=i<241:
                row=5
    return row 

'''
function to position the CRT pixel while checking if colliding with sprite positions.  
'''
def CRT_draw(image:list,cycle:int,sprite:list)->None:
    row=get_row(cycle)
    col=40 if cycle%40==0 else cycle%40
    image[row][col-1]="."
    if sprite[0]==col-1 or sprite[1]==col-1 or sprite[2]==col-1 :
        image[row][col-1]="#" 
    

def render(file):
    image=[[" "for _ in range(40)] for _ in range(6)]  #mty image 
    sprite=[0,1,2] #initial position of sprite 
    cycle=0
    f=open(file).read().split('\n')
    for line in f: 
        if line.startswith("noop"):
            cycle+=1
            CRT_draw(image,cycle,sprite)

        else:
            cycle+=1
            CRT_draw(image,cycle,sprite)
            cycle+=1
            CRT_draw(image,cycle,sprite)
            sprite[1]+=int(line[5:])
            sprite[0]=sprite[1]-1
            sprite[2]=sprite[1]+1
    return image






if __name__=="__main__":
    r=render("aoc10.txt")
    for line in r:
        ll="".join(line)
        print(ll)
