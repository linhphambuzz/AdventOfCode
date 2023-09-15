'''
function to examine if all letter in a given string are all different 
'''
def dif_test(line:str)->bool:
    if len(line)==len(set(line)):
        return True
    return False 

def both_part(file,msg=4,part2=False):
    passage=open(file).read()    
    examine_string=""
    answer=0
    
    if part2: msg=14

    for index,letter in enumerate(passage):
        examine_string+=passage[index:index+msg]
        if dif_test(examine_string)==True:
            #print(examine_string)
            answer=index+msg
            break
        else:
            examine_string=""
    return answer




if __name__=="__main__":

    assert both_part("test.txt")==7 
    assert both_part("test.txt",part2=True)==19
    print(f" part 1: {both_part('aoc6.txt')} \
             part 2: {both_part('aoc6.txt',part2=True)}")
    
