import fileinput
import collections
from functools import reduce 
from operator import mul


testInput = "testinput.txt"
input = "input.txt"

def main():
    winning_p1 = []
    winning_p2 = []
    with open(input) as file:
        lines = file.read().strip().split("\n")
        times = [int(x) for x in lines[0].split(":")[1].split(" ") if x != ""]
        distances = [int(x) for x in lines[1].split(":")[1].split(" ") if x != ""]
        bigtime = int("".join([str(x) for x in times]))
        bigdist = int("".join([str(x) for x in distances]))
        
        
        for count, time in enumerate(times):
            counter = 0
            for i in range(time):
                if i * (time - i) > distances[count]:
                   
                    counter += 1
            winning_p1.append(counter)
        
        c2 = 0
        for i in range(bigtime):
            if i * (bigtime - i) > bigdist:
                c2 += 1
    print(reduce(lambda x, y: x * y, winning_p1), c2)


if __name__ == "__main__":
    main()
