import math

input=open("aoc6.txt").readlines()

for line in input:
    l=line.split()
    if l[0]=="Time:": 
        time=int("".join(l[1:]))
    else:
        dist=int("".join(l[1:]))

print(time,dist)

"""
the goal is to find v where v*(time-v) >dist

=> -v^2 + v*time -dist > 0 
=> -(v^2 -2 * v * 1/2time + 1/4time^2 - 1/4time^2 +dist ) >0 
=> (v-1/2time)^2 < 1/4t^2 -d 
=> -sqrt(1/4t^2-d)+1/2t <v< sqrt(1/4t^2-d) +1/2t

"""

upper_bound=math.floor(math.sqrt(.25*pow(time,2)-dist)+ .5*time)

lower_bound=math.ceil(.5*time-(math.sqrt(.25*pow(time,2)-dist)))

print(1-lower_bound+upper_bound)




