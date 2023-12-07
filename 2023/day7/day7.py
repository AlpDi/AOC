import fileinput
from collections import Counter


testInput = "testinput.txt"
input = "input.txt"

strenght = "23456789TJQKA"

def get_type(card): 
    count = dict(Counter(card))
    if len(count) == 1:
        return 1
    elif len(count) == 2 and max(count.values()) == 4:
        return 2
    elif len(count) == 2 and max(count.values()) == 3:
        return 3
    elif len(count) == 3 and max(count.values()) == 3:
        return 4
    elif len(count) == 3 and max(count.values()) == 2:
        return 5
    elif len(count) == 4:
        return 6
    else:
        return 7
         
def sort_ranks(cards, bids):
    types = list(map(get_type, cards))
    zipped = list(zip(cards, types, bids))
    n = len(zipped)
    

    
    for x in range(2):
        for i in range(n):
            swapped = False

            for j in range(0, n-i-1):
               
                if zipped[j][1] < zipped[j+1][1]:
                    
                    zipped[j], zipped[j+1] = zipped[j+1], zipped[j] 
                    swapped == True
                elif zipped[j][1] == zipped[j+1][1]:
                    
                    for i in range(len(zipped[j][0])):
                        if  strenght.find(zipped[j][0][i]) > strenght.find(zipped[j+1][0][i]):
                            zipped[j], zipped[j+1] = zipped[j+1], zipped[j]
                            swapped = True
                            break
                        elif strenght.find(zipped[j+1][0][i]) > strenght.find(zipped[j][0][i]):
                            break
                            


            if (swapped == False):
                break
    return zipped




def main():
    with open(input) as file:
        result = 0
        lines = file.read().strip().split("\n")
        cards = [x.split(" ")[0] for x in lines]
        bids = [int(x.split(" ")[1]) for x in lines]
        sorted = sort_ranks(cards, bids)

        for count, card in enumerate(sorted):
            
            result = result + (count + 1) * card[2]
        print(result)


        


if __name__ == "__main__":
    main()