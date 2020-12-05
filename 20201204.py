#advent code challenge: 20201204



def readfile(filepath):
	array2D = []
	f = open(filepath, "r")
	cred = str()
	count = 0
	for line in f:
		if line[0] != '\n':
			for character in line:
				if character != '\n':
					cred = cred + character
				else: cred = cred + ' '
		else: 
			array2D.append(cred)
			cred = ''
	array2D.append(cred) #append the last credential
	return array2D


def main():
	required = ['byr', 'iyr', 'eyr', 'hgt' , 'hcl', 'ecl', 'pid']
	data = readfile("20201204_data") 
	countvalid = 0
	for i in range(len(data)):
		print(data[i])
		check = 0
		for x in range(len(required)):
			if required[x]+":" in data[i]
				check+=1
			if check == 7:
				countvalid += 1
	print("Validate Passwords: " + str(countvalid))

import time
start_time = time.time() 
main()
print("Total time: %s milliseconds" % round((time.time() - start_time)*1000, 3))