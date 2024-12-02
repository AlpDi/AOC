def part1(data):
    pass

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
