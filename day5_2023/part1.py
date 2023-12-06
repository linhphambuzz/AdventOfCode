from collections import defaultdict,namedtuple

input=open('aoc5.txt').read()
seed=defaultdict(dict)

getGap= lambda src,m_src,m_range: src-m_src if 0<=src-m_src<m_range else -10  

def parse_input(input):
    input_map=defaultdict(list)
    all=input.split('\n\n')
    for each_map in all:
        map_name,map_content=each_map.split(':')
        for content in map_content.split('\n'):
            if content:input_map[map_name].append(content.strip())
    return input_map


input_map=parse_input(input)


""" check if the src we're looking for belong to any map"""
def findMap(src,map_name):
    for line in input_map[map_name]:
        m_dest,m_src,r_=list(map(int,line.split()))
        if (g:=getGap(src,m_src,r_))>=0:
            return m_dest+g
        else:
            continue
    return src

#get all seeds
seeds=input_map['seeds'][0]

for s in seeds.split():
    s=int(s)
    soil=findMap(s,'seed-to-soil map')
    fertilizer=findMap(soil,'soil-to-fertilizer map')
    water=findMap(fertilizer,'fertilizer-to-water map')
    light=findMap(water,'water-to-light map')
    temp=findMap(light,'light-to-temperature map')
    humid=findMap(temp,'temperature-to-humidity map')
    location=findMap(humid,'humidity-to-location map')
    #update map
    seed[s]['location']=location

print(min(seed[s].get('location') for s in seed))















    







    






    

