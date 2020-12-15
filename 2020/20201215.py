#20201215

#read file get in to useable format
file = open('20201215_data', 'r')
num_list = [num.strip() for num in file.read().split(',')]
uniques = {}
print(num_list)
irange = 30000000-1
for i in range(irange):
	if i not in [0,1,2,3,4]:
		if num_list.count(num_list[i]) == 1:
			num_list.append('0')
		else: 
			if num_list.count(num_list[i]) > 1:
				last = []
				for idx,val in enumerate(num_list):
					if val == num_list[i]:
						last.append(idx)
				#print(last)
				#print(last[-1])
				#print(last[-2])
				diff = (last[-1]+1) - (last[-2]+1) 
				#print(diff)
				num_list.append(str(diff))
	if i == 200: break
	print(i)
print(num_list) 
