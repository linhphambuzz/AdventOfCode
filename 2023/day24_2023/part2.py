""""
There are 6 unknowns:   ux ,uy ,uz, uvx, uvy. uvz 
    at time t, the unknown hailstone meets with one of the input stone:
    x+vx*t=  X +Vx*t
    y+vy*t= Y +Vy*t
    z+vz*t= Z+ Vz*t
    t=(ux-x)/(vx-uvx)=(uy-y)/(vy-uvy)=(uz-z)/(vz-uvz)
This will give us 3 different equations: 
(ux-x)*(vy-uvy)=(uy-y)*(vx-uvx)
(ux-x)*(vz-uvz)=(uz-z)*(vx-uvx)
(uy-y)*(vz-uvz)=(uz-z)*(vy-uvy)

"""

import sympy

input=open("aoc24.txt").readlines()
all=len(input)
d={}
value=lambda i: int(i) if i[0]!="-" else -1*int(i[1:])
for stone_no,line in enumerate(input):
    p,v=line.strip().split(" @ ")
    d[stone_no]=[value(pp) for pp in p.split(", ")] +[value(vv) for vv in v.split(", ")]
    # print(d[stone_no])

ux,uy,uz,uvx,uvy,uvz=sympy.symbols('ux,uy,uz,uvx,uvy,uvz')

eval=list()
old_ans=None
ans=None
for idx,stone in enumerate(d):
    x,y,z,vx,vy,vz=d[stone]
    old_ans=ans
    eval.append((ux-x)*(vy-uvy)-(uy-y)*(vx-uvx))
    eval.append((ux-x)*(vz-uvz)-(uz-z)*(vx-uvx))
    ans=sympy.solve(eval)[0]
    #return results only if there's a fix solutions 
    if old_ans==ans: break

# print(ans)

p2=sum([ans[ux],ans[uy],ans[uz]])
print(p2)
    
    








