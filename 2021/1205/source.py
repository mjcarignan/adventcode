#1205

import time
import re

startTime = time.time()


#read file, get into useable format
file = open('./2021/1205/input_sample.txt', 'r')

#for each line strip the \n character, collect all values that are not delimiters, and convert to integers
ventsLines = [list(map(int, re.split(',| -> ', vent.strip()))) for vent in file.readlines()]
file.close()

#references for the coordinate lines
x1position = 0
x2position = 2
y1position = 1
y2position = 3


#Find all the lines that have the same x1 and x2 or the same y1 y2

#Loop through the smaller list for each line
straightVents = list()
map = list()

for vent in ventsLines:
    if vent[x1position] == vent[x2position] or vent[y1position] == vent[y2position]:
        straightVents.append(vent)




# for each start and end point:
for vent in straightVents:
    # for the range of difference in x potions or y positions store the range of coordinate positions
    if vent[x1position] == vent[x2position]:
        if vent[y1position] < vent[y2position]:
            start = vent[y1position]
            end = vent[y2position]+1
        else: 
            start = vent[y2position]
            end = vent[y1position]+1
        y = start
        for y in range(start,end):
            map.append([vent[x1position], y])
        
            
    elif vent[y1position] == vent[y2position]:
        if vent[x1position] < vent[x2position]:
            start = vent[x1position]
            end = vent[x2position]+1
        else: 
            start = vent[x2position]
            end = vent[x1position]+1
        x = start
        for x in range(start, end):
            map.append([x,vent[y1position]])     
print("Finished Plotting.")
print("Number of points: " + str(len(map)))

def checkio(data):
    print("Starting to remove unique points: ")
    a=[]
    for point in data:
        if data.count(point)>1:
            a.append(point)


    b=[]
    print("Starting to consolidate list: ")
    for point in a:
        if point not in b: 
            b.append(point)
    return b

print(len(checkio(map)))

    # remove unique values
    # Convert to set to get the remaining values
    # count the lenght of set 

