import re

# 2-4,6-8 will return [2,4,6,8]
def read_numbers(file):
    with open(file) as f:
        for line in f:
            line.strip()
            list_number=[int(i) for i in re.findall(r'\d+',line)]
            yield list_number 

def part1(input):
    count=0 
    for group_elf in input:
        if (group_elf[0]<=group_elf[2] and group_elf[1]>=group_elf[3])  \
        or (group_elf[0]>=group_elf[2] and group_elf[1]<= group_elf[3]): count+=1

    return count

def part2(input):
    groups=0
    no_overlap=0
    for four_elves in input:
        groups+=1
        first_group=[]
        second_group=[]
        first_group.extend(four_elves[:2])
        second_group.extend(four_elves[-2:])
        if (max(first_group)> max(second_group) and min(first_group)>max(second_group)) \
        or (max(second_group)>max(first_group) and min(second_group)>max(first_group)):
            no_overlap+=1
    return groups-no_overlap






if  __name__=="__main__":
    assert part1(read_numbers("test.txt"))==2
    print(part1(read_numbers("aoc4.txt")))

    assert part2(read_numbers("test.txt"))==4
    print(part2(read_numbers("test.txt")))


