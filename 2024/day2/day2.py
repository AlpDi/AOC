def part1(data):
    counter = 0
    for entry in data:
        rep = [int(x) for x in entry.split()]
        
        if rep == sorted(rep) or rep == sorted(rep)[::-1]:
            pairs = list(zip(rep, rep[1:]))
            diffs = list(map(lambda x: abs(x[0]-x[1]), pairs))
            isSafe = list(map(lambda x: x < 4 and x > 0, diffs))
            
            if all(isSafe): counter += 1
    return counter


    return counter

def part2(data):
    pass

def parse_input(filename):
    with open(filename) as f:
        return [line.strip() for line in f.readlines()]

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
