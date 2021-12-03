#1202

import time
import re

startTime = time.time()


#read file, get into useable format
file = open('./2021/1202/inputfull.txt', 'r')
navigations = [re.split('\s', nav.strip()) for nav in file.readlines()]
file.close()

#part 1
position = 0
depth = 0
for nav in navigations:
    match nav[0]:
        case "forward":
            position+=int(nav[1])
        case "down":
            depth+=int(nav[1])
        case "up":
            depth-=int(nav[1])

print("Part 1 answer: " + str(position*depth))

#part 2
position = 0
depth = 0
aim = 0
for nav in navigations:
    match nav[0]:
        case "forward":
            position+=int(nav[1])
            depth+=aim*int(nav[1])
        case "down":
            aim+=int(nav[1])
        case "up":
            aim-=int(nav[1])

print("Part 2 answer: " + str(position*depth))

print("Total time: %s milliseconds" % round((time.time() - startTime)*1000, 3))