import numpy as np

testInput = "testinput.txt"
input = "input.txt"




def get_axis(pattern):
    
    for count in range(1, len(pattern)):
        mismatches = 0
        for row1, row2 in zip(pattern[:count][::-1], pattern[count:]):
            for char1, char2 in zip(row1,row2):
                if char1 != char2:
                    mismatches += 1
        if mismatches == 1: 
            return  (count) * 100
            
    return 0

def get_transposed_axis(pattern):
    for count in range(1, len(pattern)):
        mismatches = 0
        for row1, row2 in zip(pattern[:count][::-1], pattern[count:]):
            for char1, char2 in zip(row1,row2):
                if char1 != char2:
                    mismatches += 1
        if mismatches == 1: 
            return  count
            
    return 0
                    
                    
#for part 2: still compare lines neighboring the potential reflection axis, if one pair is mismatched by exactly one symbol, use it instead of the original reflection 


def main():
    with open(input) as file:
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
            #print(get_axis(pattern))
            pattern_t = np.array(pattern).T.tolist()
            #print(get_transposed_axis(pattern_t))
            sum += get_axis(pattern) + get_transposed_axis(pattern_t)
        print(sum)
    
    


        
if __name__ == '__main__':
    main()