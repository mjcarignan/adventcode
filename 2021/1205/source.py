#1205

import time
import re

startTime = time.time()


#read file, get into useable format
file = open('./2021/1205/input.txt', 'r')

#for each line strip the \n character, collect all values that are not delimiters, and convert to integers
ventsLines = [tuple(map(int, re.split(',| -> ', vent.strip()))) for vent in file.readlines()]
file.close()


#references for the coordinate tuples
x1 = 0
x2 = 2
y1 = 1
y2 = 3

#find the edges of the map
x_max = max(max([xS[x1] for xS in ventsLines]), max([xS[x2] for xS in ventsLines]))
y_max = max(max([yS[y1] for yS in ventsLines]), max([yS[y2] for yS in ventsLines]))

#create and initialize the map
map = dict()
row = [0 for x in range(x_max+1)]
for y in range(y_max+1):
    map[y] = row.copy()

#get all the coordinate of the path of the vent
def getLine(vent):
    line = []
    #is it a straight line along x?
    if vent[x1] == vent[x2]:
        if vent[y1] < vent[y2]:
            start = vent[y1]
            end = vent[y2]+1
        else: 
            start = vent[y2]
            end = vent[y1]+1
        y = start

    #plot line with constant x value
        for y in range(start,end):
            line.append([vent[x1], y])  
    
    #is it a straight line along y?
    elif vent[y1] == vent[y2]:
        if vent[x1] < vent[x2]:
            start = vent[x1]
            end = vent[x2]+1
        else: 
            start = vent[x2]
            end = vent[x1]+1
        x = start
    #plot line with constant y value
        for x in range(start, end):
            line.append([x,vent[y1]])
    
    #it is a diagonal line
    else:
        #initialize range of x
        if vent[x1] < vent[x2]:
            x_range = [i for i in range(vent[x1],vent[x2]+1)]
        else: 
            x_range = [i for i in range(vent[x1],vent[x2]-1,-1)]

        #initialize range of y 
        if vent[y1] < vent[y2]:
            y_range = [i for i in range(vent[y1],vent[y2]+1)]
        else: 
            y_range = [i for i in range(vent[y1],vent[y2]-1,-1)]
        i = 0
        for i in range(len(x_range)):
            line.append([x_range[i],y_range[i]])
    return line

# plot each vent
for vent in ventsLines:
    line = getLine(vent)
    for point in line:
        map[point[0]][point[1]]+=1

#Count the points where 2 or more vents cross
count = 0
for r in map:
    count+= len([c for c in map[r] if c > 1])

print("Number of points where more than one vent cross: " + str(count))
print("Total time: %s milliseconds" % round((time.time() - startTime)*1000, 3))
