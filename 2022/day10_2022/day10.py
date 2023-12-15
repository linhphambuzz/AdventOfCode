'''
function to compute value of X given the stop_cycle 
'''
def get_signal(stop_cycle,file):
    input=open(file).read().split('\n')
    signal=1
    cycle=0
    for line in input:
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
                        if cycle==stop_cycle: return signal        
                        signal+=int(line[5:])
        else:
            return signal
        
def part1(file):
    values=[get_signal(c,file)*c for c in range(221)[20:221:40] ]
    return sum(values)






        


if __name__=="__main__":
    print(part1("test.txt"))
