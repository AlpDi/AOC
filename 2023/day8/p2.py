import fileinput

from functools import reduce 
import math


testInput = "testinput.txt"
input = "input.txt"

def get_direction(map, sequence, start):
    i = 0
    j = 0
    node = map[start]
    while True:
        if sequence[i] == "L": next = node[0]
        else: next = node[1]
        if next.endswith("Z") : break
        i += 1
        j += 1
        if i == len(sequence): i = 0
        node = map[next]
    return(j+1)

def lcm(x, y):
   if x > y:
       greater = x
   else:
       greater = y

   while(True):
       if ((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1

   return lcm   

if __name__ == "__main__":
    with open(input) as file:
        lines = file.read().strip().split("\n")
        sequence = lines[0]
        map = {}
        ghostnodes = []
        ghostpath = []
        for line in lines[2:]:
            (key, val) = line.split(" = ") 
            (left, right) = val[1:-1].split(", ")
            map[key] = (left, right)
            if key.endswith("A") : ghostnodes.append(key)
        #get_direction(map, sequence)
        for start in ghostnodes:
            ghostpath.append(get_direction(map, sequence, start))
        print(reduce(lambda a, b: math.lcm(a, b), ghostpath))
        #print(ghostpath)
        
