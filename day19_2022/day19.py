from collections import deque 
import math
import re


blueprints=dict()
max_costs=dict()
f=open("day19.txt").readlines()
for line in f:
    cost=dict()
    id,*costs=re.findall(r'\d+',line)
    costs=[int(c)for c in costs]
    cost.update({"ore":[costs[0],0,0,0]})
    cost.update({"clay":[costs[1],0,0,0]})
    cost.update({"obsidian":[costs[2],costs[3],0,0]})
    cost.update({"geode":[costs[4],0,costs[5],0]})
    max_costs[id]=[max(cost[cc][i] for cc in cost) for i in range(4)]
    blueprints.update({id:cost})

def calc_geode(blueprint,max_time,max_cost):
    resources=[0,0,0,0] #ore,clay,obsidian,geode
    bots=[1,0,0,0]
    elapsed_time=0
    states=deque()
    states.append([bots,resources,elapsed_time])
    max_geodes=0

    while states:
        bots,resources,elapsed_time=states.popleft()
        if elapsed_time==max_time: continue
    
        for nbot,each_bot in enumerate(blueprint):
            dt=[0,0,0,0]
            #calculate time to build the targeted bot from time taking to mine resources  
            for i in range(len(resources)):
                if blueprint[each_bot][i]<=resources[i]:
                    continue
                elif bots[i]:
                    dt[i]=math.ceil((blueprint[each_bot][i]-resources[i])/bots[i])
                else:
                    dt[i]=max_time+1
            
            built_time=max(dt)
        
            if built_time+1>max_time-elapsed_time: 
                continue
            else:
                new_bots=bots.copy()
                new_bots[nbot]+=1
                if new_bots[nbot]>max_cost[nbot] and nbot!=3: continue
                new_resources=[resources[j]+bots[j]*(built_time+1)-blueprint[each_bot][j] for j in range(4)]
                new_elapsed=elapsed_time+built_time+1
                #calculate ideal geodes 
                remain_time=max_time-new_elapsed
                ideal_geodes=new_resources[3]+remain_time*new_bots[3]+remain_time*(remain_time-1)/2
            
            if ideal_geodes<=max_geodes: continue

            states.append([new_bots,new_resources,new_elapsed])

        geodes=resources[3]+bots[3]*(max_time-elapsed_time)
        max_geodes=max(max_geodes,geodes)

    return max_geodes

def part1(blueprints):
    result=sum(int(bp)*calc_geode(blueprints[bp],24,max_costs[bp]) for bp in blueprints)
    return result

def part2(blueprints):
    result=1
    for _,bp in zip(range(3),blueprints):
        result*=calc_geode(blueprints[bp],32,max_costs[bp])
    return result 

if __name__=="__main__":
    print(part1(blueprints))
    print(part2(blueprints))












        

