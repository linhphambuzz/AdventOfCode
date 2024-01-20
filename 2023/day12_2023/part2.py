from functools import cache 

@cache
def cnt_func(spring,nums):
    # if all of the spring is processed, return 1 if all numbers are also processed
    if len(spring)==0:
        return 1 if len(nums)==0 else 0
    
    #if numbers are all process, return 1 is theres's no more damaged spring 
    if nums==():
        return 1 if "#" not in spring else 0
    
    # if encountered ".", skip 
    if spring[0]==".":
        return cnt_func(spring[1:],nums)
    
    cnt=0
    # if question mark 
    if spring[0]=="?":
        cnt+= cnt_func(spring[1:],nums)


    if '.' not in spring[:nums[0]] and (len(spring) == nums[0] or len(spring) > nums[0] and spring[nums[0]] != '#'):
        # print(f'at {spring[:nums[0]]} with spring len {len(spring)} and n {nums[0]}')
        cnt+=cnt_func(spring[nums[0]+1:],nums[1:])  

    return cnt 


input=open("aoc12.txt").readlines()
result=0
for line in input:
    record,nums=line.split()
    record="?".join([record]*5)
    nums=tuple(map(int,nums.split(',')))
    nums*=5
    result+=cnt_func(record,nums)
    
print(result)