import math

def readfile(filepath):
	program = []
	with open(filepath, "r") as filestream:
    	    for line in filestream:
        	    program = line.split(",")
	for i in range(0, len(program)):
		program[i] = int(program[i])
	return(program)

def processProgram(program):
	i = 0
	instruction = program[i]
	while instruction != 99:
		p1 = program[i+1]
		p2 = program[i+2]
		p3 = program[i+3]
		if program[i] == 1:
			program[p3] = program[p1] + program[p2]
		elif program[i] == 2:
			program[p3] = program[p1] * program[p2]
		i = i + 4
		instruction = program[i]
	return program

def setupProgram (program,v1,v2):
	program[1] = v1
	program[2] = v2
	return program

def main():
	working_program = readfile("20191202_data")
	targetnoun = 0
	targetverb = 0

	for noun in range(0,99):
		for verb in range(0,90):
			working_program = setupProgram(working_program,noun,verb)
			working_program = processProgram(working_program)
			if working_program[0] == 19690720:
				targetnoun = noun
				targetverb = verb
			working_program = readfile("20191202_data")
	print("Noun:" + str(targetnoun))
	print("Verb: " + str(targetverb))	
	print(100 * targetnoun + targetverb)

		
import time
start_time = time.time() 
main()
print("Total time: %s milliseconds" % round((time.time() - start_time)*1000, 2))