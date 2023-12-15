seeds = []
sts = {}
stf = {}
ftw = {}
wtl = {}
ltt = {}
tth = {}
htl = {}
currMap = None

with open('test2.txt', 'r') as file:
    for line in file:
        line = line.replace('\n', '').split(' ')
        
        
        if line[0] == 'seeds:':
            for i in range(1, len(line)):
                if line[i]:seeds.append(int(line[i]))
        elif len(line) == 3:
            currMap[(int(line[1]), int(line[1])+int(line[2])-1)] = int(line[0]) - int(line[1])
        elif len(line) == 2:
            if line[0] == 'seed-to-soil': currMap = sts
            if line[0] == 'soil-to-fertilizer': currMap = stf
            # if line[0] == 'fertilizer-to-water': currMap = ftw
            # if line[0] == 'water-to-light': currMap = wtl
            # if line[0] == 'light-to-temperature': currMap = ltt
            # if line[0] == 'temperature-to-humidity': currMap = tth
            # if line[0] == 'humidity-to-location': currMap = htl

# order = [sts, stf, ftw, wtl, ltt, tth, htl, None]

order = [sts, stf, None]


#append all seed ranges
currRanges = []
for s in range(0, len(seeds), 2):
    currRanges.append([seeds[s], seeds[s]+seeds[s+1]-1])
print(f'currRanges is {currRanges}')

adds = [0] * len(currRanges) #each adds item represent a transform number to get to location

for sr,s in enumerate(currRanges):
    print(f'processing range {s}')
    currMap = 0
    while order[currMap] != None:
        print(f'at map {currMap}')
        for m in order[currMap]:
            #seeds inside map
            if s[0] >= m[0] and s[1] <= m[1]:
                s[0] += order[currMap][m] #transform src to mapped value 
                s[1] += order[currMap][m]
                adds[sr] += order[currMap][m]
                print(f'case 1 adds[sr]= {adds[sr]}')
                break
            #map inside seeds
            elif m[0] >= s[0] and m[1] <= s[1]:
                adds += [0,0]
                currRanges.append([s[0]-adds[sr], m[0]-1-adds[sr]])
                print(f'map inside seeds addsr ={adds[sr]}')
                print(f'map inside seed, 2nd last currRanges appended is {currRanges[-1]}')
                currRanges.append([m[1]+1-adds[sr], s[1]-adds[sr]])
                print(f'map inside seed, last currRanges appended is {currRanges[-1]}')

                s[0] = m[0] + order[currMap][m]
                s[1] = m[1] + order[currMap][m]
                adds[sr] += order[currMap][m]
                break
            #overlap with seeds first
            elif s[0] < m[0] and s[1] >= m[0] and s[1] <= m[1]:
                adds += [0]
                currRanges.append([s[0]-adds[sr], m[0]-1-adds[sr]])
                s[0] = m[0] + order[currMap][m]
                s[1] += order[currMap][m]
                adds[sr] += order[currMap][m]
                break

            elif m[0] < s[0] and m[1] >= s[0] and m[1] <= s[1]:
                adds += [0]
                currRanges.append([m[1]+1-adds[sr], s[1]-adds[sr]])
                s[0] += order[currMap][m]
                s[1] = m[1] + order[currMap][m]
                adds[sr] += order[currMap][m]
                break

           
        currMap += 1
    
    
# re=min([c[0] for c in currRanges])
# print(re)


