import fileinput
import sys
import codecs

if __name__ == "__main__":
    f = codecs.open("testinput.txt", encoding='utf-8')
    contents = f.read()

    newcontents = contents.replace("|", "║").replace("-", "═").replace("L", "╚").replace("J", "╝").replace("7", "╗").replace("F", "╔")
    f.close()

    f = open("testinput.txt", "w")
    f.write(newcontents)
    f.close()