from itertools import cycle 
input=open('aoc20.txt').readlines()
def solve(zero_position:int,orders:list):
    return sum(orders[(zero_position+i)%len(input)][1] for i in (1000,2000,3000))

def shuffle(input,key=1,shuffles=1):
    numbers=[int(i)*key for i in input]
    l=len(numbers)-1
    orders=[pair for pair in enumerate(numbers)]
    to_shuffle=cycle(orders.copy())  #initial pos-number pair
    zero=(numbers.index(0),0) #pair that bears 0 in the number list 
    for _ in range(shuffles): 
        for _ in range(len(numbers)):
            pos_num=next(to_shuffle) #postion_number pair 
            old_indx=orders.index(pos_num)
            new_indx=(old_indx+pos_num[1])%l
            orders.remove(pos_num)
            orders.insert(new_indx,pos_num)
    zero_position=orders.index(zero)
    return zero_position,orders


if __name__=="__main__":
    zero_p,o=shuffle(input)
    part1=solve(zero_p,o)
    zero_p2,o2=shuffle(input,key=811589153,shuffles=10)
    part2=solve(zero_p2,o2)
    print(f"part 1 : {part1} \npart 2 : {part2}")





        

