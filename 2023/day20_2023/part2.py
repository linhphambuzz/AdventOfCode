from collections import defaultdict
from math import lcm


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
                if any (d=="rx" for d in dest.strip().split(', ')): to_send_low=name #for p2 

""" update states for all inputs of conjunction modules"""
for m in mods:
    for d in mods[m]['dest']:
        if d in conj:
            states[d]['state'].update({m:"low"})


pq=list()
press=0
to_send=None
cycle={i:None for i in states[to_send_low]['state']} #track cycles for all input of "lb"
v={i:0 for i in states[to_send_low]['state']} #track how many time high pulses are sent to lb
p2=False

while True: 
    press+=1
    bc=("button","low",["broadcaster"]) #from, p_received,dest list
    pq.append(bc)

    while pq:

        sent_fr,p_received,dests=pq.pop(0)
        
        if p_received=="high" and to_send_low in dests:
            v[sent_fr]+=1
            if not cycle[sent_fr]:
                cycle[sent_fr]=press
            else: 
                if press//cycle[sent_fr]!=v[sent_fr]: cycle[sent_fr]=press

        #if all has been seen multiple times, exit 
        if all(cnt>5 for cnt in v.values()): p2=True; break 

    
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
    
    if p2:
        ans=1
        # print(cycle)
        #find least common value of all the cycle of input
        for num in cycle.values():
            ans=lcm(ans,num)
        print(ans)
        break 
    