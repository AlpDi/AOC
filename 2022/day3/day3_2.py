import fileinput
from collections import Counter



    

    

counter = 0
sum1 = 0

with open('input.txt') as file:
    for line in file:
        if counter == 0:
            c1 = Counter(line.rstrip())
            counter = counter + 1
        elif counter == 1:
            c2 = Counter(line.rstrip())
            counter = counter + 1
        elif counter == 2:
            c3 = Counter(line.rstrip())
            dict_1 = dict(c1)
            dict_2 = dict(c2)
            dict_3 = dict(c3)

            for key in dict_1:
                    if key in dict_2 and key in dict_3:
                        if key.islower():
                            sum1 = sum1 + ord(key) - 96
                        else:
                            sum1 = sum1 + ord(key) - 38

            counter = 0
    print(sum1)