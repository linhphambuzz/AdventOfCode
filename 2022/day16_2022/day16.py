import re
from collections import defaultdict
from itertools import permutations


input=[re.findall(r'[A-Z]{2}|\d+',line) for line in open("aoc16.txt").readlines()]


def solve(input,part2=False):
  #dict for non-zero flow rates of each valve 
  flow={valve:int(flow) for valve,flow,*_ in input if flow!='0'}
  #dict that associats each non-0 flow valve to a unique binary number
  visit={valve:1<<i for i,valve in enumerate(flow)} 
  #dict to show tunnel and their neighbors
  connected_tunnel={valve:to_valves for valve,_,*to_valves in input}
  #distance between any 2 valves 
  dist={(valve,tunnel):1 if tunnel in connected_tunnel[valve] else 9999 \
              for tunnel in connected_tunnel for valve in connected_tunnel }
  
  # floyd-warshall = shortest distance for any possible pair of valves
  for k, i, j in permutations(connected_tunnel, 3):
    dist[i, j] = min(dist[i, j], dist[i, k] + dist[k, j])
  
  result=defaultdict(int)
  def get_pressure(valve,time,visited,pressure):
    result[visited]=max(result[visited],pressure)
    for tunnel in flow:
      time_remain=time-dist[(valve,tunnel)]-1
      if visit[tunnel] & visited or time_remain<=0: 
        continue
      else:
        get_pressure(tunnel,time_remain,visited=visit[tunnel]|visited,\
                     pressure=pressure+flow[tunnel]*time_remain)
    return result
  
  #part 1 
  if not part2:
    get_pressure("AA",30,0,0)
    return max(result.values())
  #part 2: most sum pressure release of 2 people   
  else: 
    ss=get_pressure("AA",26,0,0)
    part2=0
    for v1,p1 in ss.items():  
      for v2,p2 in ss.items():
        if not v1&v2: part2=max(part2,p1+p2) 
    
    return part2


if __name__=="__main__":
  print(f'part 1: {solve(input)} \
          part 2 :{solve(input,part2=True)}')

