def BWT(string):

    matrix = []
    
    l_string = [] #перетворюємо вхідний рядок на список його символів
    for i in string:
        l_string.append(i)
    
    for j in range(len(l_string)): #формуємо матрицю з усіх циклічних зсувів
        l_string = [l_string[-1]] + l_string[:-1]
        matrix.append(l_string[:])
        
    sorted_matrix = sorted(matrix) #сортуємо матрицю циклічних зсувів

    result = ''.join(row[-1] for row in sorted_matrix)

    return result

print(BWT('AGGTCAACC$'))
