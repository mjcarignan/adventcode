#1206

import time
import re

startTime = time.time()


#read file, get into useable format
file = open('./2021/1206/input.txt', 'r')
school = [int(num) for num in file.read().split(',')]
file.close()

print(school)

def modelFish(startingTimer, duration):
#loop for the duration
    fish = [startingTimer]
    for i in range(duration):
        # Loop through each fish
        for i in range(len(fish)):
            if fish[i] == 0: # if zero change to 6 and add a new timer intialized to 8
                fish.append(8)
                fish[i]=6
            else: fish[i]-=1 # decriment the fish's timer to 0
        print(len(fish))
    return len(fish)
            

#model how many fish each starting fish will generate
def getCountofOffspring(duration):
    reproductionModel = {}
    for i in range(9):
        print("Working on fish: " + str(i))
        reproductionModel[i] = modelFish(i,duration)
    return reproductionModel

model = getCountofOffspring(265)

count= 0
for fish in school:
    count+= model[fish]
print(count)
