from part1 import read_input,transpose_matrix

cache={}
def count_similar(t_matrix):
    ans=0
    col1,col2=transpose_matrix(t_matrix)
    for x in col1:
        if x not in cache:
            y=col2.count(x)
            cache.update({x:y})
        else:
            y=cache[x]
        ans+=x*y
    return ans


if __name__=="__main__":
    input_matrix=read_input("input_part1.txt")
    print(count_similar(input_matrix))






