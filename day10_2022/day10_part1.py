
#take in line number and figure what cycle we're at 
def get_signal(stop_cycle,file):
    signal=1
    cycle=0
    for line in file:
        line=line.strip()
        if cycle<stop_cycle:
            match line[0:4]:
                case "noop":
                    cycle+=1
                case "addx":
                    cycle+=1 
                    if cycle==stop_cycle:
                        return signal 
                    else:
                        cycle+=1
                        if cycle==stop_cycle:
                            return signal #signal return DURING the cycle
                        signal+=int(line[5:])
                       
    return signal

def part1(cycle_list,file):
    sum_signal=0
    for cycle in cycle_list:
        sum_signal+=cycle*get_signal(cycle,file)
    return sum_signal



if __name__=="__main__":
    file=open("aoc10.txt","r").read().split('\n')
    answer=part1([20,60,100,140,180,220],file)
    print(answer)



