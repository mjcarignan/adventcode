#Put the rules in a hash table with ranges of value
rules = {"departure location" : ([range(31,201+1),range(227, 951+1)])}
rulestest = []

file = open('20201216_rules', 'r')
rulestest = [rule.strip().split(": ") for rule in file.readlines()]
file.close()

#print(rulestest)

for i in range(len(rulestest)):
	range1 = rulestest[i][1].split(' or ')[0].split('-')
	range2 = rulestest[i][1].split(' or ')[1].split('-')
	rules[rulestest[i][0]] = ([range(int(range1[0]),int(range1[1])+1),range(int(range2[0]),int(range2[1])+1)])

# read rules in
# file = open('20201216_rules', 'r')
# for rule in file.readline().split(': '):
# 	rulestest.append(rule)
# file.close()

print(rules)

x = 31
for k,v in rules.items():
	print(x in v[0] or x in v[1])

