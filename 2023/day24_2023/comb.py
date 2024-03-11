def combinations(iterable, r):
    # combinations('ABCD', 2) --> AB AC AD BC BD CD
    # combinations(range(4), 3) --> 012 013 023 123
    pool = tuple(iterable)
    n = len(pool)
    if r > n:
        return
    indices = list(range(r))
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            print(f'r {i}')
            # print(f"i= {i} n= {n} r= {r}")
            if indices[i] != i + n - r:
                break 
        else:
            return
        indices[i] += 1
        print(f'i {i}')
        print(f'indices[i] {indices[i]} {indices}')   
        
        for j in range(i+1, r):
            indices[j] = indices[j-1] + 1
        print(f'after loop {indices}')
        yield tuple(pool[i] for i in indices)
c=combinations("abcdef",3)    
print([i for i in c])