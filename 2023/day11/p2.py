import fileinput
import numpy as np


testInput = "testinput.txt"
input = "input.txt"

def get_diff(t1, t2, er, ec):
    x1,y1 = extend(t1, er, ec)
    x2,y2 = extend(t2, er, ec)

    


    return abs(x1-x2) + abs(y1-y2)

def extend(coord, er, ec):
    x,y = coord
    tempx = x
    tempy = y

    for row in er:
        if y > row: tempy += 999999
    for col in ec:
        if x > col: tempx += 999999
    return (tempx,tempy)


def main():
    mat = []
    galaxies = []
    diffs = []
    
    
    with open(input) as file:
        for line in file:
            line = line.strip()
            line = [*line]
            mat.append(line)
    
    
    
    w,l = len(mat[0]), len(mat)
    empty_rows = [i for i, row in enumerate(mat)if all(cell == "." for cell in row)]
    empty_cols = [j for j in range(l) if all(mat[i][j] == "." for i in range(w))]
    print(empty_rows, empty_cols)

    
    
    
    
    for y in range(l):
        for x in range(w):
            if mat[y][x] == "#": 
                galaxies.append((x,y))
    
    res = [(a, b) for idx, a in enumerate(galaxies) for b in galaxies[idx + 1:]]
    for pair in res:
        diffs.append(get_diff(pair[0], pair[1], empty_rows, empty_cols))
    print(sum(diffs))
    
   


if __name__ == "__main__":
    main()
