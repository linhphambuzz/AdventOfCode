from collections import defaultdict
from copy import deepcopy

mods=defaultdict(dict)
states=defaultdict(dict) 
fields=["prefix","state","dest"]
conj=list()


"""parse the input"""
input=open('aoc20.txt').readlines()
for line in input:
    module,dest=line.strip().split(" -> ")
    name= module.strip() if module=="broadcaster" else module.strip()[1:]
    prefix=module[0] if name!="broadcaster" else None
    if prefix=="&": conj.append(name) #collect all conjunction model 
    for f in fields:
        match f:
            case "prefix":
                mods[name].update({f:prefix})
            case "state":
                states[name].update({f:"off" if prefix=="%" else {}})
            case "dest":
                mods[name].update({f:dest.strip().split(', ')})

""" update states for all inputs of conjunction modules"""
for m in mods:
    for d in mods[m]['dest']:
        if d in conj:
            states[d]['state'].update({m:"low"})


low,high=0,0
pq=list()
press=0
to_send=None
original_states=deepcopy(states)


while True: 
    press+=1
    bc=("button","low",["broadcaster"]) #from, p_received,dest list
    pq.append(bc)

    while pq:

        sent_fr,p_received,dests=pq.pop(0)
        
        if p_received=="low": 
            low+=len(dests)
        else: 
            high+=len(dests)

    
        for mod in dests: 
            if mod not in mods: continue
            #calculating next pulse to send to dest
            if p_received=="low":
                if mods[mod]['prefix']=="%":
                    to_send="high" if states[mod]['state']=="off" else "low"
                    states[mod]['state']="on" if states[mod]['state']=="off" else "off"
                    

                elif mods[mod]['prefix']=='&':
                    states[mod]['state'][sent_fr]="low"
                    to_send="high"
                else:     
                    to_send="low"
            else:
                if mods[mod]['prefix']=='&':
                    #update the state of the input 
                    states[mod]['state'][sent_fr]="high"
                    to_send="low" if all(s=="high" for s in  states[mod]['state'].values()) else "high"

            if to_send: 
                pq.append((mod,to_send,[d for d in mods[mod]['dest']]))

            to_send=None
    
    if press==1000: break
    
    
print(low*high)







        

        












    
    





  













    

    






    
