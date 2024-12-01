from collections import defaultdict
import re 

rules,part=open("input.txt").read().split("\n\n")
rules=rules.splitlines()
part=part.splitlines()

start="in"
p_dict=defaultdict(dict) 
rule_dict=defaultdict(list)
score=defaultdict(int)
#helper 
rule_name=lambda r: r[:r.find("{")]
get_rule= lambda r: r[r.find("{")+1:r.rfind("}")]

for rule in rules:
    rule=rule.strip() 
    name=rule_name(rule)
    the_rule=get_rule(rule)
    rule_dict[name]=the_rule.split(",")


for idx,p in enumerate(part):
    p=p.strip() 
    x,m,a,s=map(int,re.findall(r'\d+',p))
    p_dict[idx]=[x,m,a,s]

def part_eval(rule:list,part:list)->str:
    x,m,a,s=part
    for r_idx,r in enumerate(rule):
        if ":" not in r:
            return r
        else:
            condition,result=r.split(":") 
            if eval(condition):
                return result
            else:
                continue
        

def part1(): 
    
    for p in p_dict:
        curr_rule="in"
        while curr_rule not in ["A","R"]: 
            # print(f'current rule {curr_rule}')
            next_rule=part_eval(rule_dict[curr_rule],p_dict[p])
            # print(f'next rule {next_rule}')
            
            if next_rule in ["A","R"]: 
                if next_rule=="A" : 
                    score[p]=sum(p_dict[p])
                break
            else:
                curr_rule=next_rule

    return sum(score.values())
                 
if __name__=="__main__":
    print(part1())         

        


    
    

