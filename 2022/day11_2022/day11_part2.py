from day11_part1 import *


def monkey_inspect2(monkey_list,instruction_list,operation_list,divisible_list,true_list,false_list,count_items):
    MOD=modulo(divisible_list)
    for monkey_number,monkey in enumerate(monkey_list):
        count_items[monkey_number]+=len(monkey) #keep tracks of initial items each monkey has
        match instruction_list[monkey_number][0]:
            case "multiply number":
                monkey=[item*operation_list[monkey_number] for item in monkey]
            case "add number":
                monkey=[item+operation_list[monkey_number] for item in monkey] 
            case "square itself": 
                monkey=[item*item for item in monkey]
        mod_list=get_modulos(MOD,monkey)
        throwing2(mod_list,monkey_list,monkey_number,divisible_list,true_list,false_list)
    return count_items

def modulo(divisible_list):   #big mod=all item in divisible list product
    mod=1
    for i in divisible_list:
        mod*=i
    return mod 

def get_modulos(mod,monkey):
    mod_list=[]  # item mod (big MOD )
    for item in monkey:
        mod_list.append(item%mod)
    return mod_list   



def throwing2(mod_list,monkey_list,monkey_number,divisible_list,true_list,false_list):
    for item in mod_list:
        if item%divisible_list[monkey_number]==0:
            monkey_list[true_list[monkey_number]].append(item)
        else:
            monkey_list[false_list[monkey_number]].append(item)
        monkey_list[monkey_number].clear()
    return monkey_list



def part2(file):
    i=get_all_list(file)
    count_items={0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0}
    for j in range(10000):
        monkey_inspect2(i[0],i[1],i[2],i[3],i[4],i[5],count_items)
    ll=sorted(count_items.values())
    return ll[-1]*ll[-2]


if __name__=="__main__":
    print(part2('aoc11.txt'))

