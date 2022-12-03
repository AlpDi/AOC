import collections


with open('testInput.txt') as file:
    lines = [line.rstrip() for line in file]
        

vents = list()




for line in lines:
    start_coord = line.split(" -> ")[0]
    start_coord_x = start_coord.split(",")[0]
    start_coord_y = start_coord.split(",")[1]

    end_coord = line.split(" -> ")[1]
    end_coord_x = end_coord.split(",")[0]
    end_coord_y = end_coord.split(",")[1]
    
    if start_coord_x == end_coord_x:
        #print(start_coord, end_coord)
        for i in range(0, abs(int(start_coord_y) - int(end_coord_y)) + 1):
            if int(start_coord_y) > int(end_coord_y):
                vents.append((int(start_coord_x), int(end_coord_y) + i))
                #print(int(start_coord_x), int(end_coord_y) + i)
            else:
                vents.append((int(start_coord_x), int(start_coord_y) + i))
                #print(int(start_coord_x), int(start_coord_y) + i)
       # print("\n")
    elif start_coord_y == end_coord_y:
        #print(start_coord, end_coord)
        for i in range(0, abs(int(start_coord_x) - int(end_coord_x)) + 1):
            if int(start_coord_x) > int(end_coord_x):
                vents.append((int(start_coord_x) - i, int(start_coord_y)))
                #print(int(start_coord_x) - i, int(start_coord_y))
            else:
                vents.append((int(start_coord_x) + i, int(end_coord_y)))
                #print(int(start_coord_x) + i, int(end_coord_y))
        #print("\n")
    else:
        for j in range(0, abs(int(start_coord_y) - int(end_coord_y)) + 1):
            for i in range(0, abs(int(start_coord_x) - int(end_coord_x)) + 1):

                if int(start_coord_y) > int(end_coord_y):
                    vents.append((int(start_coord_x), int(end_coord_y) + i))
                else:
                    vents.append((int(start_coord_x), int(start_coord_y) + i))

                if int(start_coord_x) > int(end_coord_x):
                    vents.append((int(start_coord_x) - j, int(start_coord_y)))
                else:
                    vents.append((int(start_coord_x) + j, int(end_coord_y)))

print(len([item for item, count in collections.Counter(vents).items() if count > 1]))

