from collections import defaultdict 
from part1 import rule_dict
import re

flows=defaultdict(list)
regex = re.compile('([a-zA-Z]+)([<>])(\d+):([a-zA-Z]+)')
default_option=lambda rule: rule[-1]
get_rules=lambda rule: re.findall(regex,rule)[0]

init_ranges={
    'x':(1,4000),
    'm':(1,4000),
    'a':(1,4000),
    's':(1,4000)
}

for rule_name in rule_dict:
    rules=[]
    for r in rule_dict[rule_name][:-1]: 
        rules.append(get_rules(r))
    
    flows[rule_name]=rules,default_option(rule_dict[rule_name])


#helper 
def get_score(ranges:dict)->int:
    score=1
    for start,end in ranges.values():
        score*=(end-start)+1
    return score

def get_posibility(rule_name:str,ranges:dict)->int:
    
    #base case
    if rule_name=="A": 
        return get_score(ranges)
    elif rule_name=="R":
        return 0
    
    else: 

        score=0 
        invalid_condition=False
        rules,default=flows[rule_name]
    
        
        #go through each rule 
        for var, sign, num, condition_result in rules:
            num=int(num)
            start,end=ranges[var]
            
            if sign=="<":
                true_range=(start,num-1)
                false_range=(num,end)
            else: 
                true_range=(num+1,end)
                false_range=(start,num)

            #valid true range 
            if true_range[0] <= true_range[1]: 
                copy_range=ranges.copy()
                copy_range[var]=true_range
                #calculate recursively 
                score+=get_posibility(condition_result,copy_range)
            #valid false range 
            if false_range[0]<=false_range[1]: 
                ranges[var]=false_range
            #invalid range 
            else:
                invalid_condition=True 
                break

        #end of for loop 
        
        #after iterating through all rules, apply default 

        if not invalid_condition: score+=get_posibility(default,ranges)



    return score 


if __name__=="__main__":
    p=get_posibility('in',init_ranges)
    print(p)








    

    