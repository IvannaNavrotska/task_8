def BWT(string):

    matrix = []
    
    l_string = [] #перетворюємо вхідний рядок на список його символів

    for i in string:
        l_string.append(i)
        
    sorted_ = sorted(l_string) #розміщуємо в лексикографічному порядку
    
    return sorted_

print(BWT('owl'))
