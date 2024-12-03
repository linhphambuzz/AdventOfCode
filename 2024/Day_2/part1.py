import argparse 
import logging 

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def read_input(file):
    input=[[int(number) for number in line.strip().split(" ") if number] for line in open(file).read().split("\n")]
    return input

check_trend= lambda line: all(a-b>0 for a,b in zip(line,line[1:])) or \
                         all(a-b<0 for a,b in zip(line,line[1:]))

def solve(input): 
    unsafe=0
    for line in input:
        logger.debug(f"check trend: {check_trend(line)} for {line}")
        if not check_trend(line):
            unsafe+=1
            logger.debug(f"trend failed {line}")
            continue
        
        for n1,n2 in zip(line,line[1:]):
            if abs(n1-n2) not in [1,2,3]:
                logger.debug(f"distance failed {line}")
                unsafe+=1
                break
   
    return len(input)-unsafe

def test(file):
    input=read_input(file)
    assert check_trend(input[0]) == True 
    assert check_trend(input[1])== True 
    assert check_trend(input[2]) == True
    assert check_trend(input[3]) == False
    assert check_trend(input[4]) == False 

if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("file",choices=["test","real"])
    parser.add_argument("-l","--log",help="set log lvl")
    options=parser.parse_args()
    file= "test.txt" if options.file =="test" else "input.txt"
    if not options.log:
        logger.setLevel(logging.INFO)
        
    input=read_input(file)
    logger.info(f"len(input)={len(input)}")
    print(solve(input))
    
    
    if options=="test": 
        test(file)
    
    
    