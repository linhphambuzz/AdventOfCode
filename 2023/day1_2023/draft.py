import re 
D={'one':'1','two':'2','three':'3','four':'4',
   'five':'5','six':'6','seven':'7','eight':'8','nine':'9'}
t="sixtwofkh85clksveightwob"
regex=r"(?=(" + '|'.join([number for number in D]) + "))" 
t2="18 red 2 blue"
regex2=r"\s\w+)"

r=re.findall(regex2,t2)
print(r)

# r2=t2.find("red")
# print(r2)



