class ROCK:
    def __init__(self,file):
        self.coordinates=[line.strip().split("->") for line in open(file).read().splitlines()]   
        self.rocks=[[tuple(map(int,co.strip().split(','))) for co in coor] for coor in self.coordinates]
        self.cave=set()
        self.sand=set()
        self.count_sand=0
        self.floor=-1   #floor of the cave 
    def build_rock(self):
        for rock in self.rocks:
            for xy in zip(rock,rock[1:]):
                for x in range(min(xy)[0],max(xy)[0]+1):
                    for y in range(min(xy)[1],max(xy)[1]+1):
                        self.cave.add((x,y))
                        self.floor=max(y,self.floor)
        return self.cave
    #check if there's space or already occupied by rock/sand
    def is_space(self,x:int,y:int)->bool:
        if (x,y) in self.cave.union(self.sand):
            return False
        return True
    #move the sand down until it can't go further
    def move_down(self,sand_x:int,sand_y:int)->tuple:
        while sand_y<self.floor+1:
            if self.is_space(sand_x,sand_y+1):
                return self.move_down(sand_x,sand_y+1)       
            elif self.is_space(sand_x-1,sand_y+1):
                return self.move_down(sand_x-1,sand_y+1)
            elif self.is_space(sand_x+1,sand_y+1):
                return self.move_down(sand_x+1,sand_y+1) 
            else:
                self.sand.add((sand_x,sand_y)) 
                return sand_x,sand_y
        return sand_x,sand_y
    
    def CountSand(self):
        while True:
            #if the sand falls below the floor, return 
            if self.move_down(500,0)[-1]==self.floor+1:
                return len(self.sand)
            else:
                self.move_down(500,0)


def part1(file):
    r=ROCK(file)
    r.build_rock()
    return r.CountSand()

if __name__=="__main__":
    #print(part1("aoc14.txt"))
    p1=ROCK('test.txt')
    p1.build_rock()
    print(p1.floor)