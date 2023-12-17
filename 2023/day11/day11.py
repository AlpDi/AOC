import fileinput
import numpy as np


testInput = "testinput.txt"
input = "input.txt"

def get_diff(t1, t2):
    x1,y1 = t1
    x2,y2 = t2

    return abs(x1-x2) + abs(y1-y2)



def main():
    mat = []
    galaxies = []
    diffs = []
    temp = []
    
    with open(input) as file:
        for line in file:
            line = line.strip()
            line = [*line]
            if all(x == "." for x in line):
                mat.append(line)
                mat.append(line)
            else: mat.append(line)
    
    mat_t = np.array(mat).T

    for i,j in enumerate(mat_t):
        if all(x == "." for x in j):
            temp.append(j)
            temp.append(j)
        else: temp.append(j)

    mat = np.array(temp).T.tolist()
    
    
    w,l = len(mat[0]), len(mat)
    
    
    
    for y in range(l):
        for x in range(w):
            if mat[y][x] == "#": 
                galaxies.append((x,y))
    
    res = [(a, b) for idx, a in enumerate(galaxies) for b in galaxies[idx + 1:]]
    for pair in res:
        diffs.append(get_diff(pair[0], pair[1]))
    print(sum(diffs))
    
   


if __name__ == "__main__":
    main()
