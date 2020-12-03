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

def countTrees(r,d):
	treecount = 0
	tbmap = readfile("20201203_data")
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
	slope1 = countTrees(1,1) 
	slope2 = countTrees(3,1)
	slope3 = countTrees(5,1)
	slope4 = countTrees(7,1)
	slope5 = countTrees(1,2)

	print (slope1*slope2*slope3*slope4*slope5)



main()