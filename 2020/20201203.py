def readfile(filepath):
	array2D = []
	f = open(filepath, "r")
	for line in f:
		lineArray = []
		for character in line:
				if character != '\n':
					lineArray.append(character)
		array2D.append(lineArray)
	return array2D

def countTrees(tbmap,r,d):
	treecount = 0
	rowpointer = 0
	colpointer = 0
	while rowpointer <= len(tbmap)-1:
		if colpointer > len(tbmap[rowpointer])-1:
			colpointer = colpointer - (len(tbmap[rowpointer]))
		#print(colpointer)
		if tbmap[rowpointer][colpointer] == "#":
			treecount+=1
		colpointer = colpointer + r
		rowpointer = rowpointer + d
		
	return treecount

def main():
	tbmap = readfile("20201203_data")
	#print("File read: %s milliseconds" % round((time.time() - start_time)*1000, 3))

	print("Day 3, part 1: " + str(countTrees(tbmap,3,1)))
	#print("Time: %s milliseconds" % round((time.time() - start_time)*1000, 3))

	slope1 = countTrees(tbmap,1,1) 
	slope2 = countTrees(tbmap,3,1)
	slope3 = countTrees(tbmap,5,1)
	slope4 = countTrees(tbmap,7,1)
	slope5 = countTrees(tbmap,1,2)
	print("Day 3, part 2: " + str((slope1*slope2*slope3*slope4*slope5)))
	#print("Time: %s milliseconds" % round((time.time() - start_time)*1000, 3))


import time
start_time = time.time() 
main()
print("Total time: %s milliseconds" % round((time.time() - start_time)*1000, 3))