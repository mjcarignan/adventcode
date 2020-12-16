#20201215
import time
start_time = time.time() 

#read file get in to useable format
file = open('20201215_data', 'r')
num_list = [num.strip() for num in file.read().split(',')]
file.close()
uniques = {}
irange = 30000000

#populates uniques
for i in range(len(num_list)):
	uniques[int(num_list[i])] = ([i+1,i+1])

#grab last value in list
current = int(num_list[-1])

#init where to start
length = len(num_list)-1

#crunch it
for i in range(length,irange-1):
	if current in uniques:
		current = uniques[current][1]-uniques[current][0]
		if current in uniques:
			uniques[current] = ([uniques[current][1],i+2])
		else:
			uniques[current] = ([i+2,i+2])
	#print(i)

#And here's Johnny!
print(current) 
print("Total time: %s milliseconds" % round((time.time() - start_time)*1000, 3))