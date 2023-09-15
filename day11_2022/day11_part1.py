import math
import re
def parse_input(passage):
    start_item=list()
    test=list()
    lines=passage.split('\n')
    start_item=[int(i) for i in re.findall(r'\d+',lines[1])]
    #operation part
    if re.findall('[*]',lines[2]) and re.findall(r'\d+',lines[2]):
        operation="multiply number"
        test.append(operation)
        test.append(re.findall(r'\d+',lines[2])[0]) #operation number
    elif re.findall('[+]',lines[2]) and re.findall(r'\d+',lines[2]):
        operation="add number"
        test.append(operation)
        test.append(re.findall(r'\d+',lines[2])[0]) #operation number
    else:
        test.append("square itself")
        test.append("0")

    #last 3 lines: divisible by, if true test, if fall test
    last3lines=[re.findall(r'\d+',lines[3])[0],re.findall(r'\d+',lines[4])[0],re.findall(r'\d+',lines[5])[0]]
    test.extend(last3lines)
    return start_item,test #[79, 98], ['multiply', '19', '23', '2', '3'])

#after all the operation, "throwing" process what goes where
#the modulo is for part 2 to process large amount of data 
#
def throwing(monkey_list,monkey,monkey_number,divisible_list,true_list,false_list):
    for item in monkey:
        if item%divisible_list[monkey_number]==0:
            monkey_list[true_list[monkey_number]].append(item)
        else:
            monkey_list[false_list[monkey_number]].append(item)
        monkey_list[monkey_number].clear()
    return monkey_list



def get_all_list(file):
    monkey_list=[[] for _ in range(8)]
    instruction_list=[[] for _ in range(8)]
    operation_list=[[] for _ in range(8)]
    divisible_list=[[] for _ in range(8)]
    true_list=[[] for _ in range(8)]
    false_list=[[] for _ in range(8)]
    with open(file) as f:
        input=f.read().split('\n\n')
        for monkey_number,passage in enumerate(input):
            monkey_list[monkey_number]=parse_input(passage)[0]
            instruction_list[monkey_number]=parse_input(passage)[-1]
            operation_list[monkey_number]=int(instruction_list[monkey_number][1])
            divisible_list[monkey_number]=int(instruction_list[monkey_number][2])
            true_list[monkey_number]=int(instruction_list[monkey_number][3])
            false_list[monkey_number]=int(instruction_list[monkey_number][4])
    return [monkey_list,instruction_list,operation_list,divisible_list,true_list,false_list]

def monkey_inspect(monkey_list,instruction_list,operation_list,divisible_list,true_list,false_list,count_items):
    for monkey_number,monkey in enumerate(monkey_list):
        count_items[monkey_number]+=len(monkey) #keep tracks of initial items each monkey has
        match instruction_list[monkey_number][0]:
            case "multiply number":
                monkey=[math.floor(item*operation_list[monkey_number]/3) for item in monkey]
            case "add number":
                monkey=[math.floor((item+operation_list[monkey_number])/3) for item in monkey] 
            case "square itself": 
                monkey=[math.floor((item*item)/3) for item in monkey]
        throwing(monkey_list,monkey,monkey_number,divisible_list,true_list,false_list)
    return count_items

def part1(file):
    i=get_all_list(file)
    count_items={0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0}
    for j in range(20):
        monkey_inspect(i[0],i[1],i[2],i[3],i[4],i[5],count_items)
    ll=sorted(count_items.values())
    return ll[-1]*ll[-2]


if __name__=="__main__":
    print(part1("aoc11.txt"))
        




