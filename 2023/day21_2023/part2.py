from part12 import d
from math import pow

""" 26501365 = 65 + (202300 * 131)"""
# for dd in d:
#     print(f'{dd} : {d[dd]}')

#total occupied tiles after 65 steps 
first= len([co for co,v in d.items() if v in [i for i in range(65+1)[1::2]]]) #odd 
#total occupied tiles after 65+131 (from S point, cross another square) steps
second= len([co for co,v in d.items() if v in [i for i in range(65+131+1)[2::2]]]) #even 
#total occupied tiles after 65+131*2 (from S point, cross another 2 squares) steps
third=len([co for co,v in d.items() if v in [i for i in range(65+131*2+1)[1::2]]]) #odd 


def quad(y):
    # Use the quadratic formula to find the output at the large steps based on the first three data points
    a = (y[2] - (2 * y[1]) + y[0]) // 2
    b = y[1] - y[0] - a
    c = y[0]
    return (a * 202300**2) + (b * 202300) + c

print(quad([first,second,third]))