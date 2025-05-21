def BWT(string):

    matrix = []
    
    l_string = [] #перетворюємо вхідний рядок на список його символів

    for i in string:
        l_string.append(i)
    
    for j in range(len(l_string)):
        l_string = [l_string[-1]] + l_string[:-1]
        matrix.append(l_string[:])
        
    return sorted(matrix)

res = BWT('AGGTCAACC$')
for i in res:
    print(i)
