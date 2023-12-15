import re 

D={'one':'1','two':'2','three':'3','four':'4',
   'five':'5','six':'6','seven':'7','eight':'8','nine':'9'}

regex=r"(?=(" + '|'.join([number for number in D]) + "))"
sum=0 
getNumber =lambda x: D[x] if not x.isdigit() else x

for i,line in enumerate(open("test.txt").readlines()):
    line.strip()
    numbers=list(zip([i.start(0) for i in re.finditer(r'\d',line)],re.findall(r'\d',line)))
    print(numbers)
    letters=list(zip([i.start(0) for i in re.finditer(regex, line)],re.findall(regex, line)))
    print(letters)
    combined=sorted(numbers+letters)
    first,last=combined[0][-1],combined[-1][-1]
    sum+=int("".join(getNumber(first)+getNumber(last)))

print(sum)
    


