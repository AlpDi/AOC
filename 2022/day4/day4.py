

with open('input.txt') as input_file:
    lines = [line.rstrip() for line in input_file]


sum1 = 0

for line in lines:
    first_coord = line.split(",")[0]
    sec_coord   = line.split(",")[1]

    first_start = int(first_coord.split("-")[0])
    first_end   = int(first_coord.split("-")[1])

    sec_start = int(sec_coord.split("-")[0])
    sec_end   = int(sec_coord.split("-")[1])

    # if first_start >= sec_start and first_end <= sec_end or sec_start >= first_start and sec_end <= first_end  for first part

    if first_start >= sec_start and first_end <= sec_end or sec_start >= first_start and sec_end <= first_end or first_end >= sec_start and first_start <= sec_end or first_end >= sec_end and first_start <= sec_end:
        sum1 = sum1 + 1

    
    #print(first_start, first_end, sec_start, sec_end)
    print(sum1)