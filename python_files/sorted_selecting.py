capacity = {'n1': 10, 'n2': 70, 'n3': 30, 'n4': 50, 'n5': 55, 'n6': 40,
    'n7': 60, 'n8': 80, 'n9': 39, 'n12': 125, 'lt2': 800}

unit = {'bus': 20, 'swa': 53, 'eng': 35, 'chem': 68, 'hist': 90, 'phyc': 110,
    'bio': 60, 'math': 139, 'kimo': 11, 'java': 310, 'oop': 177, 'scie': 43}

s_cap = {}
s_unit = {}



def dict_sort(dest, src):
    """Sorts a dictionary according to values and copies to a new one
    
    Args: 
        src: (dict). the dictionary which is being sorted.
        dest: (dict). the new sorted dictionary.
    """

    lst = sorted(src.values())

    for item in lst:
        for cap in src:
            if item == src[cap]:
                dest[cap] = src[cap]
                del(src[cap])
                break


dict_sort(s_cap, capacity)
dict_sort(s_unit, unit)

print('\n\n{}\n\n{}\n'.format(s_unit, s_cap))

for i in s_unit:
    for j in s_cap:
        print("{:<6}{:<6}{:<6}{:<6}".format(i, s_unit[i], j, s_cap[j]))
        del(s_cap[j])
        break