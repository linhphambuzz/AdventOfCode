def read_input(file):
    matrix=[[e for e in row.strip().split(" ") if e] for row in open(file).read().strip().split("\n")]
    # print(matrix)
    return matrix 

def transpose_matrix(matrix):
    t_matrix=[[int(m[n]) for m in matrix] for n in range(len(matrix[0]))]
    # print(sorted(t_matrix[0]))
    # print(sorted(t_matrix[-1]))
    return sorted(t_matrix[0]),sorted(t_matrix[-1])
   


if __name__=="__main__":
    matrix=read_input("input_part1.txt")
    x,y= transpose_matrix(matrix)
    d=sum(abs(xx-yy) for (xx,yy) in zip(x,y))
    print(d)
   

