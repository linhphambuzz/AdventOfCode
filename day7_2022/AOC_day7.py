'''
construct a dictionaries with 
key: directory path 
values: what's in the directory, this only includes directories with sub directory and any file's size
expected from test.txt file : 

{'/home': ['a', 14848514, 8504156, 'd'], '/home/a': ['e', 29116, 2557, 62596], 
'/home/a/e': [584], '/home/d': [4060174, 8033020, 5626152, 7214296]}

'''
current_dir=""  #current directory string
dir_dict={"/home":list()} #dictionaries for all directories  

with open("aoc7.txt","r") as file: 
    input=file.read().split('\n')
    for line in input:
        size=0
        line.strip()
        if line[0]=="$": #command line 
            match line[2:]:
                case 'cd /':
                    current_dir="/home" 
                case 'cd ..': 
                # go back in directory 
                    current_dir=current_dir[:current_dir.rfind("/")]
                case 'ls':
                    pass 
                case _: #cd dir_name 
                   current_dir+="/"+line[5:] #update current path 
                    dir_dict.update({current_dir:list()})  #key:dictionary, value: what it contains
        elif line.startswith("dir"): 
            #update sub directory under main directory key
            dir_dict[current_dir].append(line.split()[-1])
        else:
            #append file size under current directory 
            dir_dict[current_dir].append(int(line.split()[0]))
                                                     
#print(current_dir)  
#print(dir_dict)  

'''
DFS recursive fucntion to get size of a given path directory 
'''
def size_of(path:str)->int: 
    sum=0
    for i in dir_dict[path]:
        if type(i)==int:
            sum+=i
        else:
            new_path=(path,i)
            sum+=size_of("/".join(new_path))
    return  sum


def part1():
    ans=0 
    for path in dir_dict:
        s=size_of(path)
        if s<=100000: 
            #print(path)
            ans+=s
    return ans



def part2():
    TOTAL_SPACE=70000000
    ans=TOTAL_SPACE
    in_used_space=size_of('/home')
    #print(in_used_space)
    FREE_SPACE_NEEDED=30000000
    to_be_clean_space= FREE_SPACE_NEEDED-TOTAL_SPACE+in_used_space
    #print(to_be_clean_space)
    for path in dir_dict:
        s=size_of(path)
        if s>=to_be_clean_space and s<in_used_space:
            if s<ans: ans=s 
    return ans 



if "__name__"==__main__:
    print(f'part 1: { part1() } \ 
            part 2 :{ part2() } 












   
