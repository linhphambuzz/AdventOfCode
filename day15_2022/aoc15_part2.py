#part 2 
from aoc15_part1 import DISTRESS

class EXCLUSION(DISTRESS):
    ZONE=4000000
    def __init__(self,file):
        super().__init__(file)
        self.read_input()
        self.right=set()
        self.left=set()
    #return false if a point is inside a source's zone
    def out_zone(self,x:int,y:int)->bool:
        for s in self.sensors:
            if (abs(s[0]-x)+abs(s[1]-y))<=self.sensors[s]:
                return False
        return True
    #boundary square: 2 line tilted right is r1 r2, l1 l2 are for lines tilted to the left
    #boundary is one unit outside of the actual boundary for a source 
    #ri,r2 have slope -1, l1,l2 have slope 1 
    # for r1,r2: y=x+b 
    #for l1,l2: y=-x+b 
    def calculate_meet_points(self):
        for sx,sy in self.sensors:
            d=self.sensors[(sx,sy)]
            self.right.add(sy+sx-d-1)
            self.right.add(sy+sx+d+1)
            self.left.add(sy-sx-d-1)
            self.left.add(sy-sx+d+1)
        return self.right,self.left
    def what_a_beacon(self):
        for r in self.right:
            for l in self.left:
                x,y=(r-l)//2,(r+l)//2
                if 0<=x<=self.ZONE and 0<=y<=self.ZONE:
                    if self.out_zone(x,y):
                        return (x,y)
    def part2(self):
        self.calculate_meet_points()
        x,y=self.what_a_beacon()
        return x*4000000+y



e=EXCLUSION('aoc15.txt')
e.part2()

           
            
