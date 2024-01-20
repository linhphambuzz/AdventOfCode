

""" function to pair up every possible stones"""
def pair(n:int):
    r=2
    pool=tuple([i for i in range(n)])
    idx=list(range(r))
    yield tuple([pool[i] for i in idx])

    while True: 
        for i in [1,0]:
            if idx[i]!=i+n-r:
                break
        else:
            return 
        idx[i]+=1 

        if i+1==1: idx[1]=idx[0]+1 
        yield tuple([pool[i] for i in idx])


input=open("test.txt").readlines()
all=len(input)
d={}
value=lambda i: int(i) if i[0]!="-" else -1*int(i[1:])
# limit=lambda x,y:200000000000000<=x<= 400000000000000 and 200000000000000<=y<=400000000000000
limit=lambda x,y:7<=x<= 27 and 7<=y<=27
no_past=lambda p,v,m: v*(m-p)>=0

for stone_no,line in enumerate(input):
    p,v=line.strip().split(" @ ")
    d[stone_no]=[value(pp) for pp in p.split(", ")] +[value(vv) for vv in v.split(", ")]

cnt=0

"""
    find line equation
    y=ax+b
    find 2 pts of x, 2 pts of y to figure out a,b
    i.e: 
    (x,y)=(19,13) with Vx,Vy=(-2,1) => (x2,y2)=(17,14)
"""

for stone_a,stone_b in pair(all):
    line_a=d[stone_a]
    x1,y1,vx1,vy1=line_a[0],line_a[1],line_a[3],line_a[4]
    line_b=d[stone_b]
    x2,y2,vx2,vy2=line_b[0],line_b[1],line_b[3],line_b[4]

    a1,a2=vy1/vx1,vy2/vx2
    print(a1,a2)
    b1,b2=y1-a1*x1,y2-a2*x2
    print(b1,b2)
    if a2==a1 and b2!=b1: #parallel
        continue
    else:
        x=(b2-b1)/(a1-a2)
        y=a1*x+b1
        if no_past(x1,vx1,x) and no_past(y1,vy1,y) and no_past(x2,vx2,x) and no_past(y2,vy2,y2):
            if limit(x,y): cnt+=1
        

print(cnt)







