import collections


with open('input.txt') as file:
    lines = [line.rstrip() for line in file]
        

vents = list()
temp_x = list()
temp_y = list()



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
        #print("\n")
    elif start_coord_y == end_coord_y:
        #print(start_coord, end_coord)
        for i in range(0, abs(int(start_coord_x) - int(end_coord_x)) + 1):
            if int(start_coord_x) > int(end_coord_x):
                vents.append((int(start_coord_x) - i, int(start_coord_y)))
                #print(int(start_coord_x) - i, int(start_coord_y))
            else:
                vents.append((int(start_coord_x) + i, int(end_coord_y)))
                #print(int(start_coord_x)+ i, int(end_coord_y))

    else:
        #print(start_coord, end_coord)
        for i in range(0, abs(int(start_coord_x) - int(end_coord_x)) + 1):
            if int(start_coord_x) > int(end_coord_x):
                temp_x.append((int(start_coord_x) - i))
                ##print(int(start_coord_x) - i)
            else:
                temp_x.append((int(start_coord_x) + i))
                ##print(int(start_coord_x) + i)

        ##print("y: ",start_coord_y, end_coord_y)
        for i in range(0, abs(int(start_coord_y) - int(end_coord_y)) + 1):
            if int(start_coord_y) > int(end_coord_y):
                temp_y.append(int(start_coord_y) - i)
                ##print(int(start_coord_y) - i)
                
            else:
                temp_y.append(int(start_coord_y) + i)
                ##print(int(start_coord_y) + i)
        
        
        for i in range(len(temp_y)):
            #print(temp_x[i], temp_y[i])
            vents.append((temp_x[i], temp_y[i]))
            #print
        
        temp_y.clear()
        temp_x.clear()
        
#print(vents)



 

print(len([item for item, count in collections.Counter(vents).items() if count > 1]))

