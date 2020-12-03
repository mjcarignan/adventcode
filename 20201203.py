import pandas as pd 

def readfile(filepath):
	array2D = []
	f = open(filepath, "r")
	for line in f:
		lineArray = []
		for i in range(0,80):
			for character in line:
				if character != '\n':
					lineArray.append(character)
		array2D.append(lineArray)
	return array2D

def countTrees(tbmap,r,d):
	treecount = 0
	rowpointer = 0
	colpointer = 0
	while rowpointer <= len(tbmap)-1 and colpointer <= len(tbmap[rowpointer]):
		if colpointer <= len(tbmap[rowpointer]):
			if tbmap[rowpointer][colpointer] == "#":
				treecount+=1
		colpointer = colpointer + r
		rowpointer = rowpointer + d
	print("Trees:" + str(treecount))
	return treecount

def main():

	tbmap = readfile("20201203_data")
	slope1 = countTrees(tbmap,1,1) 
	slope2 = countTrees(tbmap,3,1)
	slope3 = countTrees(tbmap,5,1)
	slope4 = countTrees(tbmap,7,1)
	slope5 = countTrees(tbmap,1,2)

	print (slope1*slope2*slope3*slope4*slope5)


import time
start_time = time.time() 
main()
print("Total time: %s milliseconds" % round((time.time() - start_time)*1000, 2))