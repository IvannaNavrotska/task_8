from bwt import BWT
import time


def LastToFirst(string):

    l_string = [] 
    for i in string:
        l_string.append(i)

    sorted_l_string = sorted(l_string)

    
    counts = {}
    last_row = []
    for i in l_string:
        if i not in counts:
            counts[i] = 0
        last_row.append((i, counts[i]))
        counts[i] += 1
    
    counts = {}
    first_row = []
    for i in sorted_l_string:
        if i not in counts:
            counts[i] = 0
        first_row.append((i, counts[i]))
        counts[i] += 1
        
    #словник для швидшого пошуку
    first_pos = {}
    for i, pair in enumerate(first_row):
        first_pos[pair] = i

    #last_to_first[i] = позиція last_row[i] в first_row
    last_to_first = []
    for pair in last_row:
        last_to_first.append(first_pos[pair])
        
    return last_to_first



def BWMatching(string, pat):  

    n = len(string)
    
    last_to_first = LastToFirst(string)

    top = 0
    bottom = n - 1

    while top <= bottom:
        if pat:
            symbol = pat[-1]
            pat = pat[:-1]

            pos = []
            for i in range(top, bottom + 1):
                if string[i] == symbol:
                    pos.append(i)
                
            if not pos:
                return 0

            top = last_to_first[pos[0]]
            bottom = last_to_first[pos[-1]]
        else:
            return bottom - top + 1

    return 0



def BWMatching_text():
    
    with open('input_bwm.txt', 'r') as f:
        lines = f.read().splitlines()
        text = lines[0].strip()
        pattern = lines[1].strip()

    result = BWMatching(text, pattern)

    with open('output_bwm.txt', 'w') as f:
        f.write(str(result))


if __name__ == '__main__':

    start_time = time.perf_counter()
    
    BWMatching_text()
    
    end_time = time.perf_counter()
    time = end_time - start_time
    print(f'Час виконання: {time:.6f} секунд')

    
    
