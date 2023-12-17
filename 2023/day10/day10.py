import fileinput



testInput = "testinput.txt"
input = "input.txt"

"""
╔═╗
║.║
╚═╝
"""





def get_neighbors(pipe):
    x,y = pipe
    match mat[y][x]:
        case "╔": neighbor = [ (x+1,y), (x, y+1)   ]
            
        case "╗": neighbor = [ (x-1,y), (x, y+1)   ]
            
        case "═" | "S": neighbor =  [ (x-1,y), (x+1, y)   ]
            
        case "║": neighbor =  [ (x,y-1), (x, y+1)   ]
            
        case "╝": neighbor =  [ (x-1,y), (x, y-1)   ]
            
        case "╚": neighbor =  [ (x+1,y), (x, y-1)   ]
    return [(x,y) for (x,y) in neighbor if x >= 0 and y >= 0 and y < l and x < w]
             


if __name__ == "__main__":
    mat = []
    with open(input) as file:
        mat = file.read().strip().split("\n")
    w,l = len(mat[0]), len(mat)
    
    for y in range(l):
        for x in range(w):
            if mat[y][x] == "S": start = (x,y)
    
    print(start)

    pipe = [start]
    dist = {start: 0}
    while len(pipe) > 0:
        new = pipe.pop(0)
        for coord in get_neighbors(new):
            if coord not in dist:
                pipe.append(coord)
                dist[coord] = dist[new] + 1
    print(max(dist.values()))

                


    
    
    
