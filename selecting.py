capacity = {'n1': 50, 'n2': 70, 'n3': 30, 'n4': 50, 'n5': 55, 'n6': 40,
    'n7': 60, 'n8': 80, 'n9': 40, 'n12': 125, 'lt2': 800}

unit = {'bus': 20, 'swa': 53, 'eng': 35, 'chem': 68, 'hist': 90, 'phyc': 110,
    'bio': 60, 'math': 139, 'kimo': 11, 'java': 310, 'oop': 177, 'scie': 43}

for i in unit:

    for j in capacity:

        if unit[i] >= capacity[j] - 10 and unit[i] <= capacity[j] + 10:
            print(i, unit[i], j, capacity[j])
            del(capacity[j])
            break

