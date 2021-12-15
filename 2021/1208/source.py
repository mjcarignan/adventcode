#1208

from typing import Counter
import time
import re

startTime = time.time()
filename="input.txt"

# define the unique patterns
patterns = {0:"abcefg", #6
            1:"cf", #2
            2:"acdeg", #5
            3:"acdfg", #5
            4:"bcdf", #4
            5:"abdfg", #5
            6:"abdefg", #6
            7:"acf", #3
            8:"abcdefg", #7
            9:"abcdfg", #6
            }

#part 1 
# read file, get into useable format
file = open('./2021/1208/'+filename, 'r')
signals = [re.split('\s\|\s', line.strip()) for line in file.readlines()]
file.close()
count=0
for signal in signals:
    output = [re.split('\s', signal[1])]
    for digits in output:
        for digit in digits:
            match len(digit):
                case 2:
                    count+=1
                case 3:
                    count+=1
                case 4:
                    count+=1
                case 7:
                    count+=1


print("Part 1: " + str(count))

#part 2 find the middle of the list based on the weighted average of the values

print("Part 2: " + "")
print("Total time: %s milliseconds" % round((time.time() - startTime)*1000, 3))