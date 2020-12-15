#20201215

#read file get in to useable format
file = open('20201215_data', 'r')
num_list = [num.strip() for num in file.read().split(',')]
uniques = {}
print(num_list)
irange = 30000000

for i in range(len(num_list)):
	uniques[num_list[i]] = ([i+1,i+1])

for i in range(irange-1):
	if i >= len(num_list)-1:
		if num_list[i] in uniques:
			num_list.append(str(uniques[num_list[i]][1]-uniques[num_list[i]][0]))
			if num_list[i+1] in uniques:
				uniques[num_list[i+1]] = ([uniques[num_list[i+1]][1],i+2])
			else:
				uniques[num_list[i+1]] = ([i+2,i+2])
		else:
			num_list.append('0')
			if num_list[i+1] in uniques:
				uniques[num_list[i+1]] = ([uniques[num_list[i+1]][1],i+2])
			else:
				uniques[num_list[i+1]] = ([i,i])
	print(i)
		# 	if uniques[num_list[i-1]][0] == uniques[num_list[i-1]][1]:
		# 		x = uniques[num_list[i-1]][1]
		# 		num_list.append('0')
		# 		if '0' in uniques:
		# 			uniques['0'][0] = uniques['0'][1]
		# 			uniques['0'][1] = i+1
		# 		else: uniques['0'] == ([i,i])
		# 	else: 
		# 		num_list.append(str(uniques[num_list[i-1]][1] - uniques[num_list[i-1]][0]))
		# 		if num_list[i-1] == '0':
		# 			if '0' in uniques:
		# 				uniques['0'][0] = uniques['0'][1]
		# 				uniques['0'][1] = i+1
		# 			else: uniques['0'] == ([i,i])

		# 		if num_list[i] in uniques:
		# 			uniques[num_list[i]] = ([uniques[num_list[i]][1],i+1])
		# 		else:
		# 			uniques[num_list[i]] = ([i+1,i+1])
		# else:
		# 	uniques[num_list[i-1]] = ([i,i])
		# 	num_list.append('0')
		# 	if '0' in uniques:
		# 			uniques['0'][0] = uniques['0'][1]
		# 			uniques['0'][1] = i+1
		# 	else: uniques['0'] == ([i,i])


	
	# if i not in [0,1,2,3,4]:
	# 	if num_list.count(num_list[i]) == 1:
	# 		num_list.append('0')
	# 	else: 
	# 		if num_list.count(num_list[i]) > 1:
	# 			last = []
	# 			for idx,val in enumerate(num_list):
	# 				if val == num_list[i]:
	# 					last.append(idx)
	# 			#print(last)
	# 			#print(last[-1])
	# 			#print(last[-2])
	# 			diff = (last[-1]+1) - (last[-2]+1) 
	# 			#print(diff)
	# 			num_list.append(str(diff))

print(num_list[-1]) 
