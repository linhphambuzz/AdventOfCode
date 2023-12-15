from collections import defaultdict 

input=open("aoc2.txt").readlines()
data=defaultdict(dict)
getPower= lambda score: score.get("blue")*score.get("green")*score.get("red")

def part2(input):
    sum=0 
    for n,line in enumerate(input):
        start=line.rfind(":")+1
        instructions=line[start:].strip().split(";")
        
        for cubeSet in instructions:    
            for cube in cubeSet.strip().split(","):
                number,color=cube.strip().split()    
                
                if not data[n].get(color) or data[n][color]<int(number):
                    data[n].update({color:int(number)})         
                else: 
                    continue
        sum+=getPower(data[n])

    return sum

print(part2(input))
        



                  