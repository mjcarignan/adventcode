#20201205
import pandas as pd

def getSeatMap(numrows,seatsperrow):
	row = []
	for s in range(seatsperrow):
		row.append(0)
	plane=[]
	for r in range(numrows):
		plane.append(row)
	return plane

#get data
def readFile(file):
	with open(file) as file_object:
		filedata = file_object.read().splitlines()
		return(filedata)


def getRow (bpass,rows):
	start = 0
	mid = ((rows) // 2) - 1
	end = rows
	for i in range(0,7):
		if bpass[i] == 'F':
			end = mid 
			mid = (start+end) // 2
		else:
			start = mid 
			mid = ((start + end) // 2)
	return mid

def getSeat (bpass,seatsperrow):
	start = 0
	mid = ((seatsperrow) // 2)
	end = seatsperrow
	for i in range(7,10):
		if bpass[i] == 'L':
			end = mid 
			mid = (start+end) // 2
		else:
			start = mid 
			mid = (start+end) // 2
	return mid 

def main():
	#define plane
	rows = 128
	seatsperrow = 8
	dfplane = pd.DataFrame.from_records(getSeatMap(rows,seatsperrow))

	#fill seats based on boarding passes
	boardingpasses = readFile('20201205_data')
	row = 0
	seat = 0
	seatID = 0
	count = 0
	for i in range(len(boardingpasses)):
		row = getRow(boardingpasses[i],rows)
		seat = getSeat(boardingpasses[i],seatsperrow)
		dfplane.loc[row,seat] = ((row+1) * 8) + seat
		count = i

	#Part 1
	pd.set_option('display.max_rows', None)
	print(dfplane.to_numpy().max())
	
	#Part 2
	print(dfplane)


import time
start_time = time.time() 
main()
print("Total time: %s milliseconds" % round((time.time() - start_time)*1000, 3))