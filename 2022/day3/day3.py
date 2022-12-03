import fileinput
from collections import Counter


def do_find_duplicates(x):
    l = len(x)
    string1 = x[slice(0,len(x)//2)]
    string2 = x[slice(len(x)//2, len(x))]
    c1 = Counter(string1)
    c2 = Counter(string2)
    dict_1 = dict(c1)
    dict_2 = dict(c2)

    for key in dict_1:
        if key in dict_2 :
            if key.islower():
                return ord(key) - 96
            else:
                return ord(key) - 38


count = 0
sum1 = 0
with open('input.txt') as file:
    for line in file:
        count = count + 1
        sum1 = sum1 + do_find_duplicates(line.rstrip())
        print(count, ': ', sum1)