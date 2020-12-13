#20201206
import pandas as pd 
#get data
def readFile(file):
	with open(file) as f:
		data = f.read()
		customs_rules = []

	#get each from from file
	for rule in data.split(".\n"):
		rule = rule.split("contain")
		rule[1] = rule[1].split(",")
		parent_child = []

	#get child for each parent in rule
		for child in rule[1]:
			if child[1] == 'n':
				parent_child = rule[0].replace(" bags",'').strip(), child[1:].replace(".",''), 0
			elif child[1] == '1':
				parent_child = rule[0].replace(" bags",'').strip(), child[3:].replace(" bag",''), 1
			else:
				parent_child = rule[0].replace(" bags",'').strip(), child[3:].replace(" bags",''), int(child[0:2].strip(" "))
			customs_rules.append(parent_child)

	#move to dataframe
	customs_rulesdf = pd.DataFrame(customs_rules, columns=['parentbag','child','child_count'])
	return customs_rulesdf

def findAllParents(querydf, sourcedf):
	all_parents = pd.DataFrame(columns=['parentbag','child','child_count'])
	count = 0
	if len(querydf) == 0:
		return 
	elif len(querydf) == 1:
		#print(sourcedf.loc[sourcedf['child'] == querydf.iloc[0]['parentbag']])
		return sourcedf.loc[sourcedf['child'] == querydf.iloc[0]['parentbag']]
	else: 
		for i in range(len(querydf)):
			temp = sourcedf.loc[sourcedf['child'] == querydf.iloc[i]['parentbag']]
			count += len(temp)
			#print(all_parents)
	#print(count)
	return all_parents

def findAllParents_count(querydf, sourcedf, count):
	#all_parents = pd.DataFrame(columns=['parentbag','child','child_count'])
	if len(querydf) == 0:
		return count
	else: 
		for i in range(len(querydf)):
			count+=len(sourcedf.loc[sourcedf['child'] == querydf.iloc[i]['parentbag']])
			count+=findAllParents_count(sourcedf.loc[sourcedf['child'] == querydf.iloc[i]['parentbag']], sourcedf, count)
			print(count)
		#print(all_parents)
	return count


def main():
	
	#move to dataframe
	customs_rulesdf = readFile('20201207_data')


	#Part 1 : How many outer bag colors can eventual contain a "Shiny gold bag"
	startingdf = customs_rulesdf.loc[customs_rulesdf['child'] == "shiny gold"]
	collected_parents = pd.DataFrame(columns=['parentbag','child','child_count'])
	#all_parents = pd.DataFrame(columns=['parentbag','child','child_count'])
	#for i in range(len(startingdf)):
	#all_parents = findAllParents(startingdf, customs_rulesdf)
	count = 0
	count += findAllParents_count(startingdf, customs_rulesdf, count)
	#all_parents = pd.concat([all_parents, startingdf])
	#print(all_parents)
	#print("Count: " + str(len(all_parents)))
	print("Count: " + str(count))


import time
start_time = time.time() 
main()
print("Total time: %s milliseconds" % round((time.time() - start_time)*1000, 3))