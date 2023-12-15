from collections import defaultdict
class ROCK2:
    def __init__(self,file):
        self.coordinates=[line.strip().split("->") for line in open(file).read().splitlines()]   
        self.rocks=[[tuple(map(int,co.strip().split(','))) for co in coor] for coor in self.coordinates]
        self.cave=defaultdict(list)
        #self.sand=defaultdict(list)
        self.floor=-1   #floor of the cave
        self.count=0
    def build_rocks(self):
        for rock in self.rocks:
            for xy in zip(rock,rock[1:]):
                for x in range(min(xy)[0],max(xy)[0]+1):
                    for y in range(min(xy)[1],max(xy)[1]+1):
                        self.cave[y].append(x)
                        self.floor=max(self.floor,y)
        return self.cave
    def is_space(self,x,y):
        if x in self.cave[y] or y==self.floor+2:
            return False
        return True
    def move_down(self,sand_x,sand_y):
        while sand_y<self.floor+2:
            if self.is_space(sand_x,sand_y+1): 
                return self.move_down(sand_x,sand_y+1)
            elif self.is_space(sand_x-1,sand_y+1):
                return self.move_down(sand_x-1,sand_y+1)
            elif self.is_space(sand_x+1,sand_y+1):
                return self.move_down(sand_x+1,sand_y+1)
            else:
                return (sand_x,sand_y)
    
    def part2(self):
        while True:
            sand=self.move_down(500,0)
            self.count+=1
            if sand[0]==500 and sand[-1]==0:
                return self.count
            else:
                self.cave[sand[-1]].append(sand[0])
    
r=ROCK2('aoc14.txt')
r.build_rocks()
r.part2()

