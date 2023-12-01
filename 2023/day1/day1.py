import fileinput
import re

testInput = "testinput.txt"
input = "input.txt"

num = []
totalnum = []

numbers = {
    "one" : "one1one",
    "two" : "two2two",
    "three" : "three3three",
    "four" : "four4four",
    "five" : "five5five", 
    "six" : "six6six",
    "seven" : "seven7seven",
    "eight" : "eight8eight",
    "nine" : "nine9nine"
    }

def replace_number(text, dic):
    for i,j in dic.items():
        text = text.replace(i,j)
    return text

with open(input) as file:
    for line in file:
        replaced = replace_number(line, numbers)
        for c in replaced:
            if c.isdigit():
                num.append(c)
        totalnum.append(int(str(num[0]) + str(num[-1])))
        num.clear()
    print(sum(totalnum))