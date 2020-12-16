#Put the rules in a hash table with ranges of value
rules = {}

#reading rules into a list... I really need to learn a better way of parsing lines of files
file = open('20201216_rules', 'r')
rulestest = [rule.strip().split(": ") for rule in file.readlines()]
file.close()

#moving rules to dict
for i in range(len(rulestest)):
	range1 = rulestest[i][1].split(' or ')[0].split('-')
	range2 = rulestest[i][1].split(' or ')[1].split('-')
	rules[rulestest[i][0]] = ([range(int(range1[0]),int(range1[1])+1),range(int(range2[0]),int(range2[1])+1)])


#read ticket values into  useable format
import csv
file = open('20201216_data', 'r')
tickets_list = [list(map(int,ticket)) for ticket in csv.reader(file, delimiter=',')]
file.close()


#Part 1

from itertools import chain

# change each rule range to a list of values for that concatinated set of ranges.  
# Should have done this earlier.  <facepalm>
for k,v in rules.items():
	rules[k] = list(chain(v[0],v[1]))

#contatinate ranges of all rules
valid_range = range(0)
for k,v in rules.items():
	valid_range = chain(valid_range, v)

#move all range to list... not sure how to make this part of the above block of code.
valid_range = (list(valid_range))

#add up values on tickets that match no rule
invalid = 0
for t in range(len(tickets_list)):
	for i in range(len(tickets_list[t])):
		if tickets_list[t][i] not in valid_range:
			invalid+=tickets_list[t][i]
print("Part 1: " + str(invalid))

#Part 2

#find index of invalid tickets
invalid_tickets = []

#get index of invalid tickets
for t in range(len(tickets_list)):
	for i in range(len(tickets_list[t])):
		if tickets_list[t][i] not in valid_range:
			invalid_tickets.append(t)

#drop invalid tickets
for index in sorted(invalid_tickets, reverse=True):
    del tickets_list[index]

#pull each "column" and compare it to each range set
compare_values = []
new_rules = {}
count = len(rules)
column = 0

for i in range(count):
	for t in range(len(tickets_list)):
		compare_values.append(tickets_list[t][i])
	
	column_comparison = []

	for k,v in rules.items():
		if(set(compare_values) <= set(v)):
			column_comparison.append(k)	
	
	new_rules[column] = column_comparison
	column+=1
	compare_values = []



#sorting the rules by length
new_new_rules = {}

for i in range(count):
	for item in new_rules:
		if i+1 == len(new_rules[item]):
			new_new_rules[item] = new_rules[item] 


#id columns through process of elimination
inter = []
for k,v in new_new_rules.items():
	set1 = set(v)
	set2 = set(inter)
	res = list(set1 - set2)
	new_new_rules[k] = res
	inter.append(res[0])


#update new rules
for k,v in new_new_rules.items():
	new_rules[k] = new_new_rules[k]


myticket = [127,83,79,197,157,67,71,131,97,193,181,191,163,61,53,89,59,137,73,167]

res = 1

for k,v in new_new_rules.items():
	if 'departure' in v[0]:
		res = res * myticket[int(k)]

print("Part 2: " + str(res))