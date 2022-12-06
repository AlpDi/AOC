import string

input_file = open("input.txt")
buffer = input_file.read()

def subroutine(lines, size):
    scan = []
    for i in range(len(lines)-size+1):
        scan = lines[i:i+size]
        if len(set(scan)) == size:
            print(i + size)
            return 1

   


if __name__ == "__main__":
    som = 14
    sop = 4
    subroutine(buffer, sop)
    subroutine(buffer, som)
