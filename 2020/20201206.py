#20201206

#get data
def readFile(file):
	with open(file) as f:
		data = f.read()
	return data

def main():
	data = readFile('20201206_data')
	unique_yes_per_bgroup = 0
	for bgroup in data.split("\n\n"):
		passcount = bgroup.count("\n") + 1
		answers = set(bgroup)
		if passcount > 1:
			answers.remove("\n")
		#print(bgroup  + '\n'+ str(len(answers)) + '\n')
		unique_yes_per_bgroup += len(answers)
	print(unique_yes_per_bgroup)

import time
start_time = time.time() 
main()
print("Total time: %s milliseconds" % round((time.time() - start_time)*1000, 3))