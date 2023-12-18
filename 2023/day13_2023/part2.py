input=open('aoc13.txt').read().split("\n\n")


turnBit=lambda line:{idx for idx,c in enumerate(line) if c=="#"}


def smudge_refl(matrix):
    bit_matrix=[turnBit(line) for line in matrix]
    h=len(bit_matrix)

    for idx,line in enumerate(zip(bit_matrix,bit_matrix[1:])):
        above,below=line

        if above==below:
            for i1,i2 in zip(range(idx)[idx-1::-1],range(h)[idx+2:]):
                if len(bit_matrix[i1]^bit_matrix[i2])==1:
                    if i1==0 or i2==h-1:
                        return idx+1,h-(idx+1)
                    elif all(bit_matrix[y1]==bit_matrix[y2] for y1,y2 in zip(range(idx)[i1-1:0:-1],range(h)[i2+1:])):
                        return idx+1,h-(idx+1)
                    else:
                        break
                   
                    
        
        elif len(above^below)==1:
            if all(bit_matrix[i1]==bit_matrix[i2] for i1,i2 in zip(range(idx)[idx-1::-1],range(h)[idx+2:])):
                return idx+1,h-(idx+1)
        else:
            continue

    
            

def solve(matrix):
    if not smudge_refl(matrix):
        #if not row reflection, rotate the matrix to find col reflection
        m= [[line[n_idx] for line in matrix] for n_idx in range(len(matrix[0]))]
        return smudge_refl(m)[0]
    else:
        return 100*smudge_refl(matrix)[0]


# solve(test)
if __name__=="__main__":
    p2=0
    for matrix in input:
        p2+=solve(matrix.split('\n'))
    print(p2)

