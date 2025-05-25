def inverse_BWT(string):

    #з рядка в список
    l_string = [] 
    for i in string:
        l_string.append(i)

    #сортуємо цей список
    sorted_l_string = sorted(l_string)

    #для виведення результату
    result = []

    #з'єднуємо з початковим і сортуємо
    for i, j in enumerate(sorted_l_string):
        for l, m in enumerate(l_string):
            if i == l:
                result.append(m+j)

    while len(result[0]) < len(string):
        result = sorted(result)
        result = [m + j for m, j in zip(l_string, result)]

    result = sorted(result) #$ на початку, а не в кінці!
    
    return result[0]

print(inverse_BWT('AC$GATCTG')) 


def better_inverse_BWT(string): 

    symbol = string.index('$')  

    l_string = list(string)
    n = len(l_string)
    sorted_l_string = sorted(l_string)

    counts = {}
    ranks_bwt = []
    for i in l_string:
        if i not in counts:
            counts[i] = 0
        ranks_bwt.append((i, counts[i]))
        counts[i] += 1

    counts = {}
    ranks_sorted = []
    for i in sorted_l_string:
        if i not in counts:
            counts[i] = 0
        ranks_sorted.append((i, counts[i]))
        counts[i] += 1

    T = [0] * n
    for i in range(n):
        for j in range(n):
            if ranks_bwt[i] == ranks_sorted[j]:
                T[i] = j
                break

    result = []
    pos = symbol
    for _ in range(n):
        result.append(string[pos])  
        pos = T[pos]

    return ''.join(reversed(result))

print(better_inverse_BWT('AC$GATCTG'))  
