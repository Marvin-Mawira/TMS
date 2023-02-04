import random

week = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]

for i in range(5):
    for j in range(5):
        day1 = random.choice(week)
        print(day1,'\t', week)
        week.remove(day1)
print(week)
