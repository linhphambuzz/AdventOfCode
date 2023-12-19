input=open("aoc14.txt").readlines()
w=len(input[0].strip())
#matrix rotation
m=[[line[idx] for line in input] for idx in range(w)]

re=0

for l_idx,line in enumerate(m):
    hold_idx=0
    l=list()
    for idx,c in enumerate(line):
        if c!=".": l.append(tuple([idx,c]))
    for c_idx,cc in sorted(l):
        if cc=='#':
            hold_idx=c_idx+1
        else:
            re+=len(line)-(hold_idx)
            hold_idx+=1
print(re)





