input=open("aoc9.txt").readlines()
report={}


""" the patern to find the very first number is a-b+c-d+e 
 with a,b,c,d is the first elem of each array produced to [0,0,...]"""
def turnNegative(ll):
    for idx,l in enumerate(ll):
        if idx%2==1: ll[idx]*=-1
    return ll
result=0 

for l_idx,line in enumerate(input):
    numbers=list(map(int,line.strip().split()))
    report[l_idx]=[numbers[0]]
    while not all(n==0 for n in numbers):
        hist=[sum(n) for n in zip([-n1 for n1 in numbers],[n2 for n2 in numbers[1:]])]
        # print(hist)
        report[l_idx].append(hist[0])
        numbers=hist
    neg=turnNegative(report[l_idx])
    result+=sum(neg)
    
print(result)
    
    
