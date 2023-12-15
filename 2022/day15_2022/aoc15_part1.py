from collections import defaultdict
import re
class DISTRESS:
    def __init__(self,file):
        self.file=file
        self.input=list() #parse input here
        self.pound=defaultdict(set) #key: row , value:pound position
        self.sensors=defaultdict(int) #key:sensor position, value:distance to closest beacon
        self.beacon=set() #store all beacon coordinates
        self.result=set() #beacon belong to row asked for part 1 
    def read_input(self):
        input=open(self.file).readlines()
        for line in input:
            SB=re.findall(r'-?\d+',line)
            xy=list(map(int,SB))
            distance=abs(xy[0]-xy[2])+abs(xy[1]-xy[3]) #manhattan distance 
            self.sensors[(xy[0],xy[1])]=distance
            self.beacon.add((xy[2],xy[3]))
        return self.sensors,self.beacon
    
    def count_distress(self,row:int)->int:
        for sensor in self.sensors:
            sx,sy=sensor[0],sensor[-1]
            distance=self.sensors[sensor] #manhattan distance
            d=abs(sy-row) #how far the row we're looking at from Source
            if d<=distance:
                n=distance-d
                for x in range(sx-n,sx+n+1):
                    if (x,row) not in self.beacon.union(self.sensors): self.result.add((x,row))
        return len(self.result)
    


            
d=DISTRESS("aoc15.txt")
d.read_input()
d.count_distress(2000000)



    
    
