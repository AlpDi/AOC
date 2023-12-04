import fileinput
import collections 


testInput = "testinput.txt"
input = "input.txt"

pile = []
stack = []

with open(input) as file:
    for line in file:
        line = line.strip()
        win = [x for x in line.split(":")[1].split("|")[0].split(" ") if x != '']
        num = [x for x in line.split(":")[1].split("|")[1].split(" ") if x != '']
        score = 0
        for el in num:
            if el in win:
                if (score == 0):
                    score += 1
                else:
                    score *= 2
        pile.append(score)
    print("part 1:", sum(pile))

pile2 = {}

total = []

with open(input) as file:
    for count, line in enumerate(file):
        line = line.strip()
        win = [x for x in line.split(":")[1].split("|")[0].split(" ") if x != '']
        num = [x for x in line.split(":")[1].split("|")[1].split(" ") if x != '']
        score = 0
        for el in num:
            if el in win:
                score += 1
        pile2[count +1] = score
        stack.append(count + 1)
    
    while(stack):
        i = stack[0]
        j = pile2[i]
        for x in range(j):
            stack.append(i+x+1)
        total.append(stack.pop(0))

    print(len(total))
 