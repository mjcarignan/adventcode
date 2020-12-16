#20201206
import collections
#get data
def readFile(file):
	with open(file) as f:
		data = f.read()
	return data

def main():
	data = readFile('20201206_data')

#Part 1
	unique_yes_per_bgroup = 0
	for bgroup in data.split("\n\n"):
		passcount = bgroup.strip().count('\n') + 1
		answers = set(bgroup)
		if passcount > 1:
			answers.remove("\n")
		unique_yes_per_bgroup += len(answers)
	print("Part 1: " + str(unique_yes_per_bgroup))

#Part 2
	allyes = 0
	count = [0] * 256
	for bgroup in data.split("\n\n"):
		#print(bgroup)
		passcount = bgroup.strip().count('\n') + 1
		#print("Pass: " + str(passcount))
		bgroup = bgroup.replace("\n",'')
		test = collections.Counter(bgroup) # collection count of each answer
		for value in test.values():  
			if value == passcount:
				allyes += 1 
		#print("Step: " + str(allyes))
		
	print("Part 2: " + str(allyes))
#how many == the passcount of that group many are there?



import time
start_time = time.time() 
main()
print("Total time: %s milliseconds" % round((time.time() - start_time)*1000, 3))