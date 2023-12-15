input=open("aoc6.txt").readlines()

for line in input:
    l=line.split()
    if l[0]=="Time:": 
        time=list(map(int,l[1:]))
    else:
        dist=list(map(int,l[1:]))

time_dist=[i for i in zip(time,dist)]

def cnt_race(t,d):
    cnt=0
    for hold in range(t):
        traveled=hold*(t-hold)
        if traveled>d: cnt+=1
    return cnt

record=1 

for t_d in time_dist:
    t,d=t_d
    record*=cnt_race(t,d)

print(record)


    

