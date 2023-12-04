import fileinput
import re
import collections

testInput = "testinput.txt"
input = "input.txt"

mat = []
part_nums = []
gear_nums = collections.defaultdict(list)
ratios = []

def check_neighbords(y1, x1, y2, x2, num):
    for y in range(y1, y2+1):
        for x in range(x1, x2 +1):
            if y >=0 and y < len(mat) and x >=0 and x < len(mat[y]):
                if mat[y][x] not in '1234567890.':
                    if mat[y][x] == "*":
                        gear_nums[(y,x)].append(num)
                    return True
    return False



with open(input) as file:
    for line in file:
        mat.append(line.strip())
    
for count, row in enumerate(mat):
    for match in re.finditer(r'\d+', mat[count]):
        if check_neighbords(count-1, match.start()-1, count +1, match.end(), (int(match.group(0)))):
            part_nums.append(int(match.group(0)))
            
print(sum(part_nums))
for k,v in gear_nums.items():
    if len(v) == 2:
        ratios.append((gear_nums[k])[0] * (gear_nums[k])[1] )
print(sum(ratios))
            
        
  


            