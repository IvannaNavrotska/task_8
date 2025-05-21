def BWT(string):

    l_string = [] #перетворюємо вхідний рядок на список його символів

    for i in string:
        l_string.append(i)

    return l_string

print(BWT('owl'))
