#20201205
import pandas as pd

def getSeatMap(numrows,seatsperrow):
	row = []
	for s in range(seatsperrow):
		row.append('Empty')
	plane=[]
	for r in range(numrows):
		plane.append(row)
	return plane

#get data
def readFile(file):
	with open(file) as file_object:
		filedata = file_object.read().splitlines()
		return(filedata)

def main():
	#define plane
	rows = 128
	seatperrow = 8
	dfplane = pd.DataFrame.from_records(getSeatMap(rows,seatperrow))

	#fill seats based on boarding passes
	boardingpasses = readFile('20201205_data')

	for i in range(len(boardingpasses)):
		#get row
		
		break

	dfplane.loc[0,0] = "Filled"
	print(dfplane)


	#answer day 1

	


import time
start_time = time.time() 
main()
print("Total time: %s milliseconds" % round((time.time() - start_time)*1000, 3))