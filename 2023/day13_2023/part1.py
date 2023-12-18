input=open('aoc13.txt').read().split("\n\n")

#detect row reflection 
def reflection(matrix):
    h=len(matrix)
    for idx,line in enumerate(zip(matrix,matrix[1:])):
        above,below=line
        # check if one part is reflected of other
        if above==below:
            if all(matrix[i1]==matrix[i2] for i1,i2 in zip(range(idx)[idx-1::-1],range(h)[idx+2:])):
                return idx+1,len(matrix)-(idx+1)
            

def solve(matrix):
    if not reflection(matrix):
        #if not row reflection, rotate the matrix to find col reflection
        m= [[line[n_idx] for line in matrix] for n_idx in range(len(matrix[0]))]
        return reflection(m)[0]
    else:
        return 100*reflection(matrix)[0]

if __name__=="__main__":
    p1=0
    for matrix in input:
        p1+=solve(matrix.split('\n'))
    print(p1)


