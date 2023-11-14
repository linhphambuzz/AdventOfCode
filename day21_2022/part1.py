from collections import defaultdict

input=open("aoc21.txt").readlines()
monkey_operation=defaultdict(list)
values=defaultdict(list)
operation=defaultdict(str)
for line in input:
    name=line[:line.index(":")]
    oper=(line[line.index(":")+1:]).strip()
    if len(oper.split())==1:
        monkey_operation[name]=values[name]=int(oper)
    else:
        monkey_operation[name]=oper.split()


#for m in monkey_operation:
#    print(f' name {m}: {monkey_operation[m]}')

def find_value(name):
    if values[name]:
        return values[name]
    else:
        a=find_value(monkey_operation[name][0])
        b=find_value(monkey_operation[name][2])
        o=monkey_operation[name][1]
        if o=="+":
            return a+b
        elif o=="-":
            return a-b
        elif o=="*":
            return a*b
        else: 
            return a/b

if __name__=="__main__":
    print(find_value('root'))