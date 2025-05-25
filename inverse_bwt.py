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

    result = sorted(result)
    
    return result[0]

print(inverse_BWT('сннааа'))
