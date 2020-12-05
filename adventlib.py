
#get data
def openFile(file):
	with open(file) as file_object:
		filedata = file_object.read()
		return(filedata)

# convert data to usable format
def convertData (file):
	dataList = file.splitlines()
	return(dataList)


