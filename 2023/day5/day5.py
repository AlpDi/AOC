import fileinput
import collections 
import math


testInput = "testinput.txt"
input = "input.txt"

class S2D:
    def __init__(self, source: str, dest: str):
        self.source = source
        self.dest = dest

        self.map_values: list[tuple[int,int,int]] = []

    def add(self, t: int, s: int, r: int):
        self.map_values.append([s, s+r, t])
    
    def get_dest(self, num:int):
        for start_source, end_source, dest in self.map_values:

            if start_source <= num < end_source:
                return dest + (num - start_source)
            
        return num
    

             


    

with open(input) as file:
    lines = file.read().strip().split("\n")
    seeds = [int(x) for x in lines[0].split(":")[1].split(" ") if x != ""]
    seedMaps: list[S2D] = []
    curMap = None
    for line in lines[1:]:
        if line == "":
            continue

        if line.endswith("map:"):
            source = line.split("-to-")[0]
            dest = line.split("-to-")[1].split(" ")[0]
            print(source, dest)
            curMap = S2D(source, dest)
            seedMaps.append(curMap)
        else:
            curMap.add(*[int(x) for x in line.split(" ")])

    minLoc = math.inf

    for seed in seeds:
        for sm in seedMaps:
            seed = sm.get_dest(seed)
        minLoc = min(minLoc, seed)
    print(minLoc)

            
        

       


         
        

             
    