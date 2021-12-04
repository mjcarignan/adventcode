#1203

import time
import re

startTime = time.time()


#read file, get into useable format
file = open('./2021/1203/input.txt', 'r')
report = [line.strip() for line in file.readlines()]
file.close()

#part 1

def find():
    lengthOfFile = len(report)
    length = len(report[0])
    values = [0 for i in range(length)]
    i = 0
    for line in report:
        for bit in line:
            values[i]+=int(bit)
            i+=1
        i = 0
    
    highvalue = str()
    lowvalue = str()

    for bit in values:
        if int(bit) >= lengthOfFile/2:
            highvalue+="1"
            lowvalue+="0"
        else:
            highvalue+="0"
            lowvalue+="1"
    return [highvalue, lowvalue]

v = find()

print("Part 1 answer: " + str(int(v[0], base=2)*int(v[1], base=2)))



#part 2

def findMostCommon(index, list):
    lengthOfList = len(list)
    value = 0
    for line in list:
            value+=int(line[index])  #summing the column of bits
    if value >= lengthOfList/2: #check to see which is the most common value is either a 1 or 0
        return("1")
    else:
        return("0")

def findLeastCommon(index, list):
    lengthOfList = len(list)
    value = 0
    for line in list:
            value+=int(line[index]) #summing the column of bits
    if value < lengthOfList/2: #check to see which is the least common value is either a 1 or 0
        return("1")
    else:
        return("0")

oxygen = report.copy()
co2 = report.copy()

i = 0
while i in range(len(oxygen[0])) and len(oxygen)!=1:
    commonValue = findMostCommon(i,oxygen)
    oxygen = [line for line in oxygen if commonValue in line[i]] 
    i+=1

i = 0

while i in range(len(co2[0])) and len(co2)!=1:
    leastCommonValue = findLeastCommon(i,co2)
    co2 = [line for line in co2 if leastCommonValue in line[i]] 
    i+=1


print("Part 2 answer: " + str(int(oxygen[0], base=2)*int(co2[0], base=2)))

print("Total time: %s milliseconds" % round((time.time() - startTime)*1000, 3))