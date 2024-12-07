def part1(data):
    res = 0
    rules = data[0]
    updates = data[1]
    for update in updates:
        order = {}
        nums = [int(x) for x in update.split(",")]
        for i in range(len(nums)):
            order[nums[i]] = i
        result = is_ordered(order, rules)
        if result[0]:
            res += result[1]
    return res


def is_ordered(order, rules):
    flag = False
    for rule in rules:
        one = int(rule[:2])
        two = int(rule[3:])
        if one in order and two in order:
            if order[one] < order[two]:
                pass
                flag = True
            else: 
                #print(one,two,update)
                flag = False
                break
        else: pass
    return flag, list(order)[len(list(order))//2]

def order(order, rules):
    result = is_ordered(order, rules)
    if result[0]:
        return result[1]
    else:
        pass
        

    





def part2(data):
    pass

def parse_input(filename):
    with open(filename) as f:
        return ([x.strip().split("\n") for x in f.read().split("\n\n")])

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
