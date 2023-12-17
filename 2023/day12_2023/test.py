def nbconf( record, groups ):

    # Cas de base
    if len(groups) == 0: # plus de # à placer
        if '#' not in record: print("returning 1")
        return 1 if '#' not in record else 0
    if sum(groups) + len(groups) - 1 > len(record): # plus assez de place pour les #
        print("not enough space")
        return 0

    # Récursion
    if record[0] == '.': # si on démarre par un .
        print("encounter dot, moving to the right 1 char")
        return nbconf( record[1:], groups)

    nb = 0
    if record[0] == '?': # ... par un ?
        print("encouter question, add recursion move record 1 to the right")
        nb += nbconf( record[1:], groups) # possibilités en mettant un . à la place du ?

    # Possibilités avec le premier groupe de # au début
    # On veut tout le début sans . et on veut qu'à l'indice taillebloc il n'y ait pas un #
    # Alors on peut placer tout le 1er bloc au début (obligatoire si on commence ou veut commencer par un #)
    if '.' not in record[:groups[0]] and (len(record) <= groups[0] or len(record) > groups[0] and record[groups[0]] != '#'):
            print(f' record {record} group {groups}')
            nb += nbconf( record[groups[0]+1:], groups[1:]   )

    return nb

input=open("test.txt").readlines()
test=input[0].strip()
record,nums=test.split()
nums=tuple(map(int,nums.split(',')))

nbconf(record,nums)