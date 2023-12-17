import fileinput



testInput = "testinput.txt"
input = "input.txt"
arrangements = 0

def get_arrangements(springs: list, groups):
    print(springs, groups)
    if not springs  and not groups: arrangements += 1
    elif (not springs and groups) or (springs and not groups): return 0

    
    cur = springs[0]
    if cur == ".": 
        springs.pop(0)
        get_arrangements(springs, groups)
    if cur == "?":
        temp = springs
        springs[0] = "."
        get_arrangements(springs, groups)
        temp[0] = "#"
        get_arrangements(temp, groups)
    if cur == "#":
        if len(springs) >= groups[0]:
            if all(x != "." for x in springs[:groups[0]-1]):
                for i in range(groups[0]):
                    springs.pop(i)
                groups.pop(0)
                get_arrangements(springs, groups)
    



def main():
    with open(testInput) as file:
        lines = file.read().strip().split("\n")
        for line in lines:
            springs, groups = line.split(" ")
            groups = [int(x) for x in groups.split(",") if x != ""]
            springs = [*springs]
            get_arrangements(springs, groups)
        print(arrangements)


if __name__ == "__main__":
    main()