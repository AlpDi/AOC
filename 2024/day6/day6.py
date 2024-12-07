def part1(data):
    start = ()
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == "^":
                start = i, j
                break
    print(has_obstacle(data, "up", start))


def has_obstacle(data, dir, pos):
    steps = 0
    if dir == "up":
        for i in range(pos[0]+ 1):
            if data[pos[0] - i][pos[1]] == "#":
                return pos[0] - i, pos[1], steps
            else:
                steps += 1
    return False

def part2(data):
    pass

def parse_input(filename):
    with open(filename) as f:
        return [list(el) for el in [line.strip() for line in f.readlines()]
]
def main():
    # Test input
    test_data = parse_input('testinput.txt')
    print("Part 1 Test:", part1(test_data))
    print("Part 2 Test:", part2(test_data))
    
    # Real input
    """ data = parse_input('input.txt')
    print("Part 1:", part1(data))
    print("Part 2:", part2(data)) """

if __name__ == "__main__":
    main()
