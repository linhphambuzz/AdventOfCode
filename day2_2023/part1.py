input=open("aoc2.txt").readlines()

C={"red":12,"green":13,"blue":14}

cnt_cubes=lambda x: False if int(x[0]) > C[x[-1]] else True 

def part1(input):
    score=0 
    for n,line in enumerate(input):
        start=line.rfind(":")+1
        instructions=line[start:].strip().split(";")
       
        if all(list(cnt_cubes(c.strip().split()) for cubeSet in instructions\
                                            for c in cubeSet.strip().split(",") )):
                                       
            score+=(n+1)
            # print(f'{n+1} passed')
        else:
            # print(f'{n+1} failed')
            continue
    return score



print(part1(input))




