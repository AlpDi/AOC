import numpy as np

testInput = "testinput.txt"
input = "input.txt"




def get_axis(pattern):
    for count, line in enumerate(pattern):
        if count + 1 < len(pattern):
            if line == pattern[count+1]:
                dist = min([len(pattern[:count]), len(pattern[count+2:])])
                #print(dist, len(pattern[:count]), len(pattern[count+2:]))
                #print(pattern[count-dist:count], (pattern[count+2:count+2+dist])[::-1])
                if pattern[count-dist:count] == (pattern[count+2:count+2+dist])[::-1]:
                    return (count + 1) * 100
    return 0

def get_transposed_axis(pattern):
    for count, line in enumerate(pattern):
        if count + 1 < len(pattern):
            if line == pattern[count+1]:
                dist = min([len(pattern[:count]), len(pattern[count+2:])])
                #print(dist, len(pattern[:count]), len(pattern[count+2:]))
                #print(pattern[count-dist:count], (pattern[count+2:count+2+dist])[::-1])
                if pattern[count-dist:count] == (pattern[count+2:count+2+dist])[::-1]:
                    return (count + 1)
    return 0
                    
                    
#for part 2: still compare lines neighboring the potential reflection axis, if one pair is mismatched by exactly one symbol, use it instead of the original reflection 


def main():
    with open(testInput) as file:
        patterns = [[]]
        count = 0
        lines = file.read().strip().split("\n")
        for line in lines:
            line = [*line]
            if line == []:
                count += 1
                patterns.append([])
            else: patterns[count].append(line)
        
        sum = 0

        for pattern in patterns:
            print(get_axis(pattern))
            pattern_t = np.array(pattern).T.tolist()
            print(get_transposed_axis(pattern_t))
            sum += get_axis(pattern) + get_transposed_axis(pattern_t)
        print(sum)
    
    


        
if __name__ == '__main__':
    main()