import fileinput
from functools import cache



testInput = "testinput.txt"
input = "input.txt"

@cache
def get_arrangements(springs, groups):
    #print(springs, groups)
    if not groups:
        return 0 if "#" in springs else 1
    if not springs:
        return 1 if not groups else 0
    
    
    result = 0

    if springs[0] == '?' or springs[0] == '.':
        result += get_arrangements(springs[1:], groups)
    if springs[0] == '?' or springs[0] == '#':
        if (
            groups[0] <= len(springs)
            and "." not in springs[: groups[0]]
            and (groups[0] == len(springs) or springs[groups[0]] != '#')
        ):
            result += get_arrangements(springs[groups[0] + 1 :], groups[1:])

    return result


def main():
    with open(input) as file:
        lines = file.read().strip().split("\n")
        arrangements = 0
        arrangements2 = 0
        for line in lines:
            springs, groups = line.split(" ")
            groups = [int(x) for x in groups.split(",") if x != ""]
            groups = tuple(groups)
            arrangements += get_arrangements(springs, groups)
            #print(get_arrangements(springs, groups))

            groups = groups * 5
            springs = '?'.join([springs] * 5)
            arrangements2 += get_arrangements(springs, groups)
        print(arrangements, arrangements2)  
            


if __name__ == "__main__":
    main()