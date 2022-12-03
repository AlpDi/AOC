import fileinput



# A: Rock - 1
# B: Paper - 2
# C: Scissor - 3
# L: 0
# D: 3
# W: 6
# X: need lose
# Y: need draw
# Z: need win


scores = {
    "A X": 3,
    "A Y": 4,
    "A Z": 8,
    "B X": 1,
    "B Y": 5,
    "B Z": 9,
    "C X": 2,
    "C Y": 6,
    "C Z": 7
}

with open('input.txt') as file:
    sum1 = sum(scores[line.rstrip()] for line in file)
    print(sum1)