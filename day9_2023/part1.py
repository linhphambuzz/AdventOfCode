input=open("aoc9.txt").readlines()
report={}

for l_idx,line in enumerate(input):
    numbers=list(map(int,line.strip().split()))
    report[l_idx]=numbers[-1]
    
    while not all(n==0 for n in numbers):
        hist=[sum(n) for n in zip([-n1 for n1 in numbers],[n2 for n2 in numbers[1:]])]
        report[l_idx]+=hist[-1]
        numbers=hist

print(sum(report.values()))
    



