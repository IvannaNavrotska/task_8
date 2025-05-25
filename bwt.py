import time

def BWT(string):

    matrix = []

    #перетворюємо вхідний рядок на список його символів
    l_string = [] 
    for i in string:
        l_string.append(i)

    #формуємо матрицю з усіх циклічних зсувів
    for j in range(len(l_string)): 
        l_string = [l_string[-1]] + l_string[:-1]
        matrix.append(l_string[:])

    #сортуємо матрицю циклічних зсувів
    sorted_matrix = sorted(matrix) 

    #повертаємо останній стовпчик матриці
    result = ''.join(row[-1] for row in sorted_matrix) 

    return result


def BWT_text():

    with open('input.txt', 'r') as f:
        text = f.read().strip()
        
    result = BWT(text)

    with open('output.txt', 'w') as f:
        f.write(result)


if __name__ == '__main__':

    start_time = time.perf_counter()
    
    BWT_text()
    
    end_time = time.perf_counter()
    time = end_time - start_time
    print(f'Час виконання: {time:.6f} секунд')

