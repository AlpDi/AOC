import re

def part1(data):



    ins = re.findall("mul\([0-9]*,[0-9]*\)", data)

    nums = [x[4:-1].split(",") for x in ins]
    nums = [[int(item) for item in sublist] for sublist in nums]

    result = sum(list(map(lambda x: x[0] * x[1], nums)))


    return result

def part2(data):

    result = 0

    ins = re.findall("mul\([0-9]*,[0-9]*\)|do\(\)|don't\(\)", data)

    flag = True

    for match in ins:
        if match == "do()":
            flag = True
        elif match == "don't()":
            flag = False
        else:
            if flag:
                x,y = map(int, match[4:-1].split(","))
                result += x*y

    return result

def parse_input(filename):
    return open(filename).read()

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
