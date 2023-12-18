testInput = "testinput.txt"
input = "input.txt"



def get_axis(pattern):
    for count, line in enumerate(pattern):
        if count + 1 < len(pattern) - 1:
            if line == pattern[count+1]:
                print(line)
                print(pattern[count+1])



def main():
    with open(testInput) as file:
        patterns = [[]]
        count = 0
        lines = file.read().strip().split("\n")
        for line in lines:
            if line == "":
                count += 1
                patterns.append([])
            else: patterns[count].append(line)
        
        for pattern in patterns:
            get_axis(pattern)
    
    


        
if __name__ == '__main__':
    main()