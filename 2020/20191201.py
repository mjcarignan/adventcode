#import libs``
import math

#get data
def openFile(file):
	with open(file) as file_object:
		filedata = file_object.read()
		return(filedata)

# convert data to usable format
def convertData (file):
	dataList = file.splitlines()
	return(dataList)

#round down function
def round_down(n, decimals=0):
    multiplier = 10 ** decimals
    return math.floor(n * multiplier) / multiplier

#calculate fuel for a value
def get_fuelneed (value):
	fuelNeeded = round_down(value / 3) - 2
	return (int(fuelNeeded))
	

#report total

def main():
	file = openFile('20191201_data')
	data = convertData(file)
	total_fuel = 0	
	for element in data:
		print("Element: " + element)
		value = int(element)
		TotalNeedPer = 0
		while value > 0:
			value = get_fuelneed(value)
			print ("Need: " + str(value))
			if value > 0:
				TotalNeedPer = TotalNeedPer + value
				print(TotalNeedPer)
		total_fuel = total_fuel + TotalNeedPer

	print(total_fuel)

main()
