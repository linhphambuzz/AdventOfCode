from math import pow
from collections import defaultdict


m={"1":1,"2":2,"0":0,"-":-1,"=":-2}

total=0 
for line in open("aoc25.txt").readlines():
    line=line.strip()
    s=[(len(line)-idx-1,c) for idx,c in enumerate(line)]
    total+=sum(pow(5,i[0])*m[i[1]] for i in s )

minus=lambda x: [-2,1] if x==3 else [-1,1] 

""" convert base 10 to base 5"""
def base_5(num):
    l=list()
    while num:
        l.append(num%5)
        num//=5
    return l

 
""" convert sum to snapfu number"""
def snapfu(num:list):
    d={i:n for i,n in enumerate(num)}
    # print(f'new dict {d}')
    if all(n not in (3,4) for n in d.values()):
        return d
    
    t3,t4=list(),list() #list of idx that is 3,4
    for idx,v in enumerate(num):
        if v==3: 
            d[idx]=-2
            t3.append(idx)
        if v==4:
            d[idx]=-1
            t4.append(idx)
    p_v=[(p,v) for p,v in d.items()]
    for p,v in p_v:
        if p in t3+t4: d[p+1]+=1
    
    return snapfu(d.values())

s=snapfu(base_5(int(total)))   
print(s)  







        



