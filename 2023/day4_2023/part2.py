from collections import defaultdict

input=open("aoc4.txt").readlines()
cards=defaultdict(int)
cards.update({idx:1 for idx in range(1,len(input)+1)})

for idx,line in enumerate(input):
    point=0
    line.strip()
    line=line[line.index(":")+2:]
    win_part,my_part=line.split("|")
    win_part,my_part=list(map(int,win_part.strip().split())),list(map(int,my_part.strip().split()))
    for w in win_part:
        if w in my_part: point+=1
    
    initial_cards=cards[idx+1]
    for p in range(1,point+1):
        cards[idx+1+p]+=initial_cards

print(sum(cards.values()))


