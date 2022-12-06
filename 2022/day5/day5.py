import re
with open('inputTest.txt') as input_file:
    lines = [line.rstrip() for line in input_file]


def load(lines):
    crates = []
    for line in lines:
        if line.strip().startswith("1"):
            break
        for count, val in enumerate(line):
            if val.isupper():
                count = int((count - 1) / 4)
                while len(crates) <= count:
                    crates.append([])
                crates[count].append(val)
    for i in range(len(crates)):
        crates[i] = crates[i][::-1] 
    return crates


def crane(crates, lines, crane_name):
    for line in lines:
        if line.strip().startswith("move"):
            move = re.sub("[^0-9 ]","", line).lstrip()
            size = int(move.split("  ")[0])
            source = int(move.split("  ")[1])
            dest = int(move.split("  ")[2])
            #print(size, source, dest)
            if crane_name == "CrateMover 9000":
                for _ in range(size):
                    crates[dest - 1].append(crates[source-1].pop())
            elif crane_name == "CrateMover 9001":
                bigStorage = []
                for _ in range(size):
                    bigStorage.append(crates[source-1].pop())
                crates[dest - 1] += bigStorage[::-1]
            #print(crates)
    return crates



if __name__ == "__main__":
    crates_b = load(lines)
    #print(crates_b)
    #crates_whack = crane(crates_b, lines,"CrateMover 9000")
    crates_efficint = crane(crates_b, lines,"CrateMover 9001") 
    
    #for i in range(len(crates_efficint)):
        #print(crates_efficint[i].pop())
