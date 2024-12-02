def part1(data):
    """ left = sorted([int(x.split()[0]) for x in data])
    right = sorted([int(x.split()[1]) for x in data]) """
    
    left = sorted(int(x.split()[0]) for x in data)
    right = sorted(int(x.split()[1]) for x in data)
       
    dist = sum([abs(x-y) for x,y in zip(left,right)])
    return dist


from collections import Counter
        

def part2(data):
    """ left = [int(x.split()[0]) for x in data]
    right = [int(x.split()[1]) for x in data]

    occurences = {}

    for num in right:
        if num in occurences:
            occurences[num] += 1
        else:
            occurences[num] = 1

    return sum([x * occurences[x] for x in left if x in occurences]) """

    left, right = zip(*(map(int, x.split()) for x in data))

    occurences = Counter(right)

    return sum(x * occurences[x] for x in left)

    
       

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
