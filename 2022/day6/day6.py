import string

input_file = open("inputTest.txt")
buffer = input_file.read()

def subroutine(lines):
    scan = []
    sop = 4
    som = 14
    for i in range(len(lines)-som+1):
        scan = lines[i:i+som]
        print(set(scan))
        if len(set(scan)) == som:
            print(scan,"\n")
            print(lines.find(scan) + som)
            return 1

   


if __name__ == "__main__":
    subroutine(buffer)
