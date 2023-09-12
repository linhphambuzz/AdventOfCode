#rule for part 2
look_for={
    'X':'lose',
    'Y':'draw',
    'Z':'win'
}
point_wholeround={
    'lose':0,
    'draw':3,
    'win':6
}
oppo_A={
    'win':2,
    'draw':1,
    'lose':3
}
oppo_B={
    'win':3,
    'draw':2,
    'lose':1
}
oppo_C={
    'win':1,
    'draw':3,
    'lose':2
}

'''
Return point based off what opponent plays and rules
'''
def total_point(opponent,rule): 
    point=0
    match opponent: 
        case 'A':
            point+=oppo_A[look_for[rule]] + point_wholeround[look_for[rule]]
            return point 
        case 'B': 
            point+=oppo_B[look_for[rule]] + point_wholeround[look_for[rule]]
            return point 
        case 'C': 
            point+=oppo_C[look_for[rule]] + point_wholeround[look_for[rule]]
            return point

if __name__=="__main__":
    with open("aoc2.txt") as lines: 
        tot_point=0
        for line in lines:
            match=line.strip()
            tot_point+=total_point(match[0],match[-1])
    print(tot_point)    
