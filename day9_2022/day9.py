""" 
D_vector=Head_vector - Tail vector
--> Head_vector=Tail vector + D_vector
For the tail vector to catch up with head vector, D_vector with x or y component's absolute value greater than 2 
needs to be changed to 1 so that vector head and vector tail stay next to each other. 
On the other hand, sign of D_vector x and y component needs to be preserved 

function process_complex is to do the above:
e.g: D_vector=2-1j => 1-1j 
             =1+2j => 1+1j 
"""

def process_complex(C_number):
   re=C_number.real
   ima=C_number.imag
   if abs(re)>1 and abs(ima)>1:
      re=1 if re>0 else -1
      ima=1 if ima>0 else -1
   elif abs(re)>1 and abs(ima)<=1: 
      re=1 if re>0 else -1
   else: #abs(ima) >1 
      ima=1 if ima>0 else -1
   return complex(re,ima)

MOVE={"R":1j,"L":-1j,"U":1,"D":-1}

def part1(input):
   file=open(input,"r").read().split('\n')
   Tvisit=set() 
   H_p=complex(0,0) #inital coordinate head 
   T_p=complex(0,0) # tail 
   for line in file:
      line=line.strip()
      direction,steps=line.split()
      for move in range(int(steps)):
         H_p+=MOVE[direction]
         d=H_p-T_p  #the different vector bw head and tail 
         if abs(d.real)>1 or abs(d.imag)>1: 
            T_p+=process_complex(d)
         Tvisit.add(T_p)
   
   return(len(Tvisit))

'''
Function to continuosly check 2 adjacent nodes 
'''

knots=[complex(0,0)]*10 

def checkknots(head_indx):
    tail_indx=head_indx+1
    h=knots[head_indx]
    t=knots[tail_indx]
    d=h-t #the different vector bw head and tail 
    if abs(d.real)>1 or abs(d.imag)>1: 
        t+=process_complex(d)
        knots[tail_indx]=t
    return knots

def part2(input):
   file=open(input,"r").read().split('\n')
   Tvisit=set()
   for line in file: 
      line.strip()
      direction,steps=line.split()
      for move in range(int(steps)):
         knots[0]+=MOVE[direction]    #knots[0] is head
         for node_indx in range(9):
            checkknots(node_indx) #each knot following knots[0] acting as a head following by a tail
            Tvisit.add(knots[9])

   return(len(Tvisit))
    

if __name__=="__main__":
   print(f'part 1: {part1("aoc9.txt")}\npart 2: {part2("aoc9.txt")}')
                





