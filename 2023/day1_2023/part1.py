import re 

def part1(file): 
    input= open(file).readlines()
    sum=0 
    for line in input:
        line.strip()
        l=re.findall(r'\d',line)
        sum+=int("".join([l[0],l[-1]]))
    return sum  
    

if __name__=="__main__":
    print(part1("aoc1.txt"))


    
    

    
