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
#contatinate ranges of all rules
from itertools import chain
valid_range = range(0)
for k,v in rules.items():
	valid_range = chain(valid_range, v[0],v[1])

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

invalid_tickets = []

#find index of invalid tickets
for t in range(len(tickets_list)):
	for i in range(len(tickets_list[t])):
		if tickets_list[t][i] not in valid_range:
			invalid_tickets.append(t)

#drop invalid tickets
for index in sorted(invalid_tickets, reverse=True):
    del tickets_list[index]



