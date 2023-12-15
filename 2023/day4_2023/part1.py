import math 


input=open('aoc4.txt').readlines()

result=0 

calculate_point=lambda p: 0 if p-1<0 else pow(2,p-1)

for line in input:
    point=0
    line=line.strip()
    line=line[(line.index(":"))+2:]
    win_part,my_part=line.split("|")
    win_part,my_part=list(map(int,win_part.strip().split())),list(map(int,my_part.strip().split()))
    for w in win_part:
        if w in my_part: point+=1
    result+=calculate_point(point)
    

print(result)
    
    


