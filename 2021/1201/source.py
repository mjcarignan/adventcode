import time

startTime = time.time()


#read file, get into useable format
file = open('./2021/1201/inputfull.txt', 'r')
depths = [int(depth.strip()) for depth in file.readlines()]

#part 1
compare = 0
lastdepth = depths[0]
for depth in depths:
    if lastdepth < depth:
        compare+=1
    lastdepth = depth
print('Answer part 1: ' + str(compare))


#part 2
length = len(depths)
comparewindows = 0
windows = []
for i in range(length-2):
    windows.append(depths[i]+depths[i+1]+depths[i+2])



lastwindow = windows[0]
for window in windows:

    if lastwindow < window:
        #print(str(window) + ' increase')
        comparewindows+=1
    lastwindow = window
print('Answer part 2: ' + str(comparewindows))

print("Total time: %s milliseconds" % round((time.time() - startTime)*1000, 3))