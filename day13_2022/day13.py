class COMPARE:
    def __init__(self,file):
        self.file=file
        self.pair_collections=open(file).read().split('\n\n')
        self.order={1:0,-1:0,0:0}
        self.packets=list()
    
    def read_input(self): 
        for pair in self.pair_collections: 
            [pair1,pair2]=pair.split('\n')
            [pair1,pair2]=[eval(pair1),eval(pair2)]
            self.packets.append([pair1,pair2])
        return self.packets           
    #compare 2 item 
    def item_pair(self,pair1_item,pair2_item):
        result=0
        if type(pair1_item)==int and type(pair2_item)==int:
            result+=self.cp_2int(pair1_item,pair2_item)
        elif type(pair1_item)==int and type(pair2_item)!=int:
            result+=self.cp_int_list(pair1_item,pair2_item)
        elif type(pair1_item)!=int and type(pair2_item)==int:
            result+=self.cp_list_int(pair1_item,pair2_item)
        else: 
            result+=self.cp_2list(pair1_item,pair2_item)
        return result
    #compare 2 int
    def cp_2int(self,x,y):
        if x<y: 
            return 1
        elif x>y:
            return -1
        else:
            return 0
    #compare int & list 
    def cp_int_list(self,x_int,y_list):
        return self.cp_2list([x_int],y_list)
    #compare list and int 
    def cp_list_int(self,x_list,y_int):
        return self.cp_2list(x_list,[y_int])
    #compare 2 list 
    def cp_2list(self,list_x,list_y):
        count_x=len(list_x)
        count_y=len(list_y)
        while min(count_x,count_y)!=0:
            for x,y in zip(list_x,list_y):
                count_x-=1
                count_y-=1
                if self.item_pair(x,y)!=0:  #2 equal element 
                    return self.item_pair(x,y)
        return self.cp_2int(count_x,count_y)

#part 1 
def part1(file):
    result=0
    g=COMPARE(file)
    input=g.read_input()
    for number,packets in enumerate(input):
        if g.cp_2list(*packets)==1:
            result+=(number+1)
    return result

#part2 
def part2(file): 
    divider1,divider2=[[2]],[[6]]
    d1,d2=0,0 
    g2=COMPARE(file)
    all=[p for p_group in g2.read_input() for p in p_group]  #flatter packets
    for item in all:
        if g2.cp_2list(item,divider1)==1: d1+=1
    all.insert(d1,divider1) #put divider 1 in the list 
    for item in all:
        if g2.cp_2list(item,divider2)==1: d2+=1 

    return (d1+1)*(d2+1)


if __name__=="__main__":
    print(f' part1: {part1("aoc13.txt")} \n part2:{part2("aoc13.txt")}')
    