def part1(file):
    with open(file,"r") as lines:
        point=0
        for line in lines:
            match=line.strip()
            if match[-1]=='X' and match[0]=='B': 
                point+=1
            if match[-1]=='X' and match[0]!='B':
                point+=1
                if match[0]=='A':
                    point+=3
                else: 
                    point+=6
            if match[-1]=='Y' and match[0]=='C': 
                point+=2
            if match[-1]=='Y' and match[0]!='C':
                point+=2
                if match[0]=='B':
                    point+=3 
                else: 
                    point+=6
            if match[-1]=='Z' and match[0]=='A':
                point+=3
            if match[-1]=='Z' and match[0]!='A':
                point+=3
                if match[0]=='C':
                    point+=3 
                else: 
                    point+=6
    return point

if __name__=="__main__":
    print(part1("aoc2.txt"))




