def part1(data):
    counter = 0
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == 'X':
                counter = is_horMatch(data, i, j, counter)
                counter = is_vertMatch(data, i, j, counter)
                counter = is_diaMatch(data, i, j, counter)
    return counter

def is_horMatch(data, y, x,c):
    if x < len(data[y]) - 3:
        if data[y][x+1]=='M' and data[y][x+2] =='A' and data[y][x+3]=='S':
            #print(f"h {y} {x}")
            c+=1
    if x > 2:
        if data[y][x-1]=='M' and data[y][x-2] =='A' and data[y][x-3]=='S':
            #print(f"rh {y} {x}")
            c+=1
    return c

def is_vertMatch(data, y, x,c):
    if y < len(data) - 3:
        if data[y+1][x]=='M' and data[y+2][x] =='A' and data[y+3][x]=='S':
            #print(f"v {y} {x}")
            c+=1
    if y > 2:
        if data[y-1][x]=='M' and data[y-2][x] =='A' and data[y-3][x]=='S':
            #print(f"rv {y} {x}")
            c+=1
    return c

def is_diaMatch(data, y, x,c):
    if x < len(data[y]) - 3 and y < len(data) - 3:
        if data[y+1][x+1]=='M' and data[y+2][x+2] =='A' and data[y+3][x+3]=='S':
                #print(f"ddr {y} {x}")
                c += 1
    
    if x > 2 and y < len(data) - 3:
        if data[y+1][x-1]=='M' and data[y+2][x-2] =='A' and data[y+3][x-3]=='S':
                #print(f"ddl {y} {x}")
                c +=1

    if x > 2 and y > 2:
        if data[y-1][x-1]=='M' and data[y-2][x-2] =='A' and data[y-3][x-3]=='S':
                #print(f"dul {y} {x}")
                c+=1 

    if x < len(data[y]) - 3 and y > 2:
        if data[y-1][x+1]=='M' and data[y-2][x+2] =='A' and data[y-3][x+3]=='S':
                #print(f"dur {y} {x}")
                c+=1
    return c 




def part2(data):
    pass

def parse_input(filename):
    with open(filename) as f:
        return [list(el) for el in [line.strip() for line in f.readlines()]]

def main():
    # Test input
    test_data = parse_input('testinput.txt')
    print("Part 1 Test:", part1(test_data))
    print("Part 2 Test:", part2(test_data))
    
    # Real input
    data = parse_input('input.txt')
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))

if __name__ == "__main__":
    main()
