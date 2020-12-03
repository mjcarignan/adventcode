#import libs``
import math
import adventlib as advl
import pandas as pd

def main():
#import data

	data = pd.read_csv('20201202_data' , header=None, sep=' ')
	data.columns = ['rule' , 'test' , 'pw']
	
	#clean data
	new = data.rule.str.split("-", n = 1, expand = True)
	data['pos1'] = new[0].astype(int)
	data['pos2']= new[1].astype(int)
	new = data.test.str.split(":", n = 1, expand = True)
	data.test = new[0]
	print("File read in:  %s milliseconds" % math.trunc((time.time() - start_time)*1000))
#select 
#	goodpw = data[data.pw.str.count('x') >= 1 ]
	count=0
	for index, row in data.iterrows():
		if (
			(row.pw[row.pos1-1] == row.test) & (row.pw[row.pos2-1] != row.test)
			|
			(row.pw[row.pos1-1] != row.test) & (row.pw[row.pos2-1] == row.test)
			):
			count+=1
	print ("Valid Passwords: " + str(count))
# count rows where test appears in pw >= min and <= max 	


#		if (row.pw.count(row.test) >= row.minO) & (row.pw.count(row.test) <= row.maxO):
#			count+=1


import time
start_time = time.time()
main()
print("Total time: %s milliseconds" % math.trunc((time.time() - start_time)*1000))