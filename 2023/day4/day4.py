import fileinput
import collections 


testInput = "testinput.txt"
input = "input.txt"

pile = []
#stack = []

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

cards = [1 for _ in open(input)]
total = 0
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
        

        """ stack.append(count + 1)
    
    while(stack):
        i = stack[0]
        j = pile2[i]
        for x in range(j):
            stack.append(i+x+1)
            
        stack.pop(0)
        total += 1

    print(total) """ #whacko solution
    print(pile2)
    print(cards)
    for k in pile2:
        for i in range(pile2[k]):
            cards[k + i] += cards[k]
    print(sum(cards))
    

 