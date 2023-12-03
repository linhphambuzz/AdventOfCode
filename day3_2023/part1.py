from collections import defaultdict 
import re

input=open("aoc3.txt").readlines()
numbers=defaultdict(set)
symbols=defaultdict(set)

"""
update numbers and symbols with their positions
"""
def update_dict(input):
    for line_idx,line in enumerate(input):
        line=line.strip()
        all_num,all_sym=re.findall(r'\d+',line), re.findall(r'[^(\.|\d+)]|\+',line)
        idx_num=[(i.start(0),i.end(0)) for i in re.finditer(r'\d+',line)]
        numbers.update({(line_idx,idx):int(n) for n,idx in zip(all_num,idx_num)})
        idx_sym=[(i.start(0),i.end(0)) for i in re.finditer(r'[^(\.|\d+)]|\+',line)]
        symbols.update({(line_idx,idx[0]):s for s,idx in zip(all_sym,idx_sym)})
    return numbers,symbols

"""get all neigrbor surrounding numbers"""
getNeighbor= lambda row,col,len:[(row-1,y) for y in range(col-1,len+1)] + \
                                [(row+1,y) for y in range(col-1,len+1)] +  [(row,col-1),(row,len)]
   
                                
def part1(input):
    result=0
    numbers,symbols=update_dict(input)

    for n in numbers:
        row,(col,len)=n  
        if any(symbols.get(idx) for idx in getNeighbor(row,col,len)):
            result+=int(numbers[n])

    return result



print(part1(input))