import fileinput
from collections import Counter


testInput = "testinput.txt"
input = "input.txt"

def get_direction(map, sequence):
    node = map["AAA"]
    i = 0
    j = 0
    while True:
        if sequence[i] == "L": next = node[0]
        else: next = node[1]
        if next == "ZZZ": break
        i += 1
        j += 1
        if i == len(sequence): i = 0
        node = map[next]
    print(j+1)

            

if __name__ == "__main__":
    with open(input) as file:
        lines = file.read().strip().split("\n")
        sequence = lines[0]
        map = {}
        for line in lines[2:]:
            (key, val) = line.split(" = ") 
            (left, right) = val[1:-1].split(", ")
            map[key] = (left, right)
        get_direction(map, sequence)
        
