from collections import Counter,defaultdict


LABEL=["A","K","Q","T","9","8","7","6","5","4","3","2","1","J"]

input=[tuple(i.strip().split()) for i in open("aoc7.txt").readlines()]
c_dict=defaultdict(list)

for c_b in input:
    c,b=c_b
    # print(f'original card {c}')
    sorted_label=sorted(Counter(c).values(),reverse=True)
    j_cnt=c.count("J")

    if j_cnt:
        potential_group=[(tuple(sorted_label))]
        #replacing J  with any other characters, get the best one 
        for char in set(c):
            if char!="J": 
                temp_c=c.replace(char,"J")
                potential_group.append(tuple(sorted(Counter(temp_c).values(),reverse=True)))
    # get the highest valued group 
        gr=sorted(potential_group)[-1]
        c_dict[gr].append([c,b])
    else:
        c_dict[tuple(sorted_label)].append([c,b])

type_order=sorted(c_dict.keys())
all=list()
result=0
def is_lower(card_x,card_y):
    for x,y in zip(card_x,card_y):
        if LABEL.index(x)>LABEL.index(y):
            return True
        elif LABEL.index(x)==LABEL.index(y):
            continue
        else: 
            return False


def partition(arr,low,high):
    pivot=arr[high][0]
    i=low-1
    for j in range(low,high):
        if is_lower(arr[j][0],pivot):
            i+=1
            (arr[i],arr[j]) =(arr[j],arr[i])

    (arr[i+1],arr[high])=(arr[high],arr[i+1])
    return i+1  
    

def quick_sort(arr,low,high):
    if low<high:
        pi=partition(arr,low,high)
        quick_sort(arr,low,pi-1)
        quick_sort(arr,pi+1,high)


for type in type_order:
    quick_sort(c_dict[type],0,len(c_dict[type])-1)
    all+=c_dict[type]


for idx,bid in enumerate(all):
    result+=(idx+1)*int(bid[1])

print(result)
            









