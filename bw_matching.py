from bwt import BWT

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
    first_pos = { pair: i for i, pair in enumerate(first_row) }

    #last_to_first[i] = позиція last_row[i] в first_row
    last_to_first = [ first_pos[pair] for pair in last_row ]

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

            positions = [i for i in range(top, bottom + 1) if string[i] == symbol]
            if not positions:
                return 0

            top = last_to_first[positions[0]]
            bottom = last_to_first[positions[-1]]
        else:
            return bottom - top + 1

    return 0



string = 'AAGGGCGTCGGTGC'
pattern = 'GG'
bw_string = BWT(string)

print(BWMatching(bw_string, pattern))

