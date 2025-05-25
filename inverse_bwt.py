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

    #термінальний символ
    symbol = string.index('$')  

    #з рядка в список
    l_string = [] 
    for i in string:
        l_string.append(i)
        
    n = len(l_string)
    
    sorted_l_string = sorted(l_string)

    #підрахунок появи символів у вхідному рядку(останній стовпчик)
    counts = {}
    last_row = []
    for i in l_string:
        if i not in counts:
            counts[i] = 0
        last_row.append((i, counts[i]))
        counts[i] += 1

    #підрахунок появи символів у відсортованому рядку(перший стовпчик)
    counts = {}
    first_row = []
    for i in sorted_l_string:
        if i not in counts:
            counts[i] = 0
        first_row.append((i, counts[i]))
        counts[i] += 1

    #побудова масиву T
    T = [0] * n
    for i in range(n):
        for j in range(n):
            if last_row[i] == first_row[j]:
                T[i] = j
                break

    result = []

    for _ in range(n):
        result.append(string[symbol])  
        symbol = T[symbol]
        
    #для порядку
    return ''.join(reversed(result))

print(better_inverse_BWT('AC$GATCTG'))  
