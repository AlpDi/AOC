import fileinput

testInput = "testinput.txt"
input = "input.txt"

red = []
green = []
blue = []
IDs = []
powers = []

rl = 12
gl = 13
bl = 14


#p1: extracts r,g,b values from each subset of a game, appends them to a list and checks if max(color) of each game is under the given threshhold
#p2: extracts r,g,b values from each subset of a game and multiplies the maxima of each color per game

with open(input) as file:
    for line in file:
        cubes = [i.split(",") for i in line.split(":")[1].split(";")]
        for cube in cubes:
            for color in cube:
                if "red" in color: red.append(int(color[1] + color[2]))
                if "green" in color: green.append(int(color[1] + color[2]))
                if "blue" in color: blue.append(int(color[1] + color[2]))
        print(red, green, blue)
        powers.append(max(red) * max(green) * max(blue)) #computes powers for part 2
        if max(red) <= rl and max(green) <= gl and max(blue) <= bl: #checks if values are under threshhold for part 1
            IDs.append(int(line.split(":")[0].split(" ")[1])) 
        red.clear()
        green.clear()
        blue.clear()
    print(sum(IDs))
    print(sum(powers))
            