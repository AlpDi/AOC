import fileinput


testInput = "testinput.txt"
input = "input.txt"








if __name__ == "__main__":
    with open(input) as file:
        lines = file.read().strip().split("\n")
        sums = []
        for line in lines:
            nums = [int(x) for x in line.split(" ") if x != ""]
            nums.reverse() #remove for part 1
            print(nums)
            next = []
            lasts = []
            while True:
                if all(i == 0 for i in nums):
                    break
                next = []
                for c, num in enumerate(nums[1:]):
                    next.append(num - nums[c])
                lasts.append(nums[-1])
                print(next)
                nums = next
            sums.append(sum(lasts))
        print(sum(sums))
                


            
