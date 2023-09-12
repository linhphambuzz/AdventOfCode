#function to calculate priority 
def convert_to_ascii(item):
    if ord(item)>=97:    
        return ord(item)-96 #lower case
    else: 
        return ord(item)-38  #upper case

def part1(file):
    sum_priority=0
    with open(file,'r') as ruttlesacks: 
        for bag in ruttlesacks: 
            for i in range(int(len(bag)/2)):
                for j in range(int(len(bag)/2),int(len(bag))):
                    if bag[i]==bag[j]:
                        sum_priority+=convert_to_ascii(bag[i])
                        break
                if bag[i]==bag[j]: break                         
    return sum_priority

#for part 2, find common letter among group 3 elves 
def find_badge(sack1,sack2,sack3):
    for s in sack1:
        if s in sack2 and s in sack3:
            #print(s)
            return s 
        

def part2(file):
    sum=0
    f=list(open(file))
    f=[[ff,f[f.index(ff)+1],f[f.index(ff)+2]]for ff in f[::3]]
    for group in f:
        badge=find_badge(*group)
        sum+=convert_to_ascii(badge)
    return sum


    


if __name__=="__main__":
   assert part1("test.txt")==157
   print(part1("aoc3.txt"))

   assert part2("test.txt")==70
   print(part2("aoc3.txt"))

