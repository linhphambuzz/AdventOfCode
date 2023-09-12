import re
import copy 

#take input1:all pilars, iput2: list of instructions 
def read_file(file):
    with open(file) as f:
        input1,input2=f.read().split("\n\n")
    return input1.split('\n'),input2.split('\n') 


'''function to take in a string line and find the slot of the letter in a row, if there's any letter at all
each slot occupies 4 spaces including '[','letter',']' and a white space
find ']' position, add 1 for the white space then divide by 4 to find the letter position 
expected:  (1, 'N') (2, 'C') itterated from zip'''

def find_my_slot(string_line):
    position_list=[] #list contains all positions of all letters in the string, indx start at 1 
    letter_list=[]
    for num,char in enumerate(string_line):
        if char==']':
            position= (num+1+1)/4   # +1 to find white space, +1 for indx offset  
            position_list.append(int(position))
            letter_list.append(string_line[num-1]) #minus 1 because the letter is left of  "]"

    return zip(position_list,letter_list)


'''
function to build matrix from the pillars input 
e.g: pillars: ['    [D]    ', '[N] [C]    ', '[Z] [M] [P]', ' 1   2   3 '] 
1. go through each row in pillars, find position numbers for letters in that row 
2. position of the letter in the matrix: row= same row in input, column is position calculted from 
find_my_slot()
expected:

[' ', 'D', ' ']
['N', 'C', ' ']
['Z', 'M', 'P']

 '''


def create_stacks(pillars): 
    columns=int((len(pillars[-1])+1)/4)
    rows= len(pillars)-1
    matrix=[[" "for _ in range(columns)] for _ in range(rows)]
    for row_number,line in enumerate(pillars): 
        pos_let=find_my_slot(line)
        for position,letter in pos_let:
           matrix[row_number][position-1]=letter   #construct the matrix from input
    return matrix 

'''
this function is essentially a transpose of matrix for the 
matrix produced by the function above. 

['Z', 'N']
['M', 'C', 'D']
['P']

'''

def transpose(matrix):
    columns=len(matrix[-1])
    rows=len(matrix)
    stacks=[[] for _ in range(columns)] 
    for index in range(columns): 
        for i in range(-1,-(rows+1),-1):   #fill bottom up 
            if matrix[i][index]!=" ":
                stacks[index].append(matrix[i][index]) 

    return stacks



#part1 
def part1(instructions,stacks):
    answer=[]
    for guide in instructions: 
        number_of_blocks,from_stack,to_stack= map(int,re.findall(r'\d+',guide))
        for i in range(number_of_blocks):
            stacks[to_stack-1].append(stacks[from_stack-1].pop()) 
    for i in stacks:
        answer.append(i[-1])
    return answer 


#part2 
def part2(instructions,stacks):
    answer=[]
    for guide in instructions: 
        number_of_blocks,from_stack,to_stack= map(int,re.findall(r'\d+',guide))
        #blocks moved in bulk
        moving_blocks=stacks[from_stack-1][-number_of_blocks:]
        #transport blocks in order to new stack 
        for i in moving_blocks:
            stacks[to_stack-1].append(i)
        #remove moved blocked the old stacks
        stacks[from_stack-1]=stacks[from_stack-1][:len(stacks[from_stack-1])-number_of_blocks]
    
    for i in stacks:
        answer.append(i[-1])

    return answer      





if __name__=="__main__": 
    pillars,instructions=read_file("aoc5.txt")
    m=create_stacks(pillars)
    original_stacks=transpose(m)
    #part 1 : deepcopy so the original stacks can be reused for part 2 
    s1=copy.deepcopy(original_stacks)
    print(part1(instructions,s1))

    #part 2 
    s2=original_stacks[:]
    print(part2(instructions,s2))

    

