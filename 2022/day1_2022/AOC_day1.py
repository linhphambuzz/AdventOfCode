'''
function to generate lists inside a big list, each list in the big list
represents food item that one elf carries
'''
def all_elves(file):
    with open(file) as f:
        elves=f.readlines() #readlines out put string list
        food=[] #big list 
        elf=[] #small list
    
        for item in elves: 
            if item == '\n':
                food.append(elf)        
                elf=[]
            else:
                elf.append(int(item.strip('\n')))
    food.append(elf)
    
    return food 

'''
what elf carries the most food?
'''
def part1(food):
    sum_food=map(sum,food)
    return max(sum_food)

'''
sum of 3 elevs carrries the most food
'''
def part2(food):
    list_food=sorted(map(sum,food))
    return sum(list_food[:-3])


if __name__="__main__":
    print(f"sum of maximum food carried: {part1(all_elves('aoc1.txt'))}")
    print(f"sum of 3 elves with max food: {part2(all_elves('aoc1.txt'))}")


    





