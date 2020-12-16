import time

STARTTIME = time.time()

file = open('20201207_data', 'r')
fileContents = [rule.strip() for rule in file.readlines()]

# create a dict such that it looks like this:
# {
#   'shinygold': {'1': 'darkolive', '2': 'vibrantplum'},
#   'darkolive': {'3': 'fadedblue', '4': 'dottedblack'}
# }
Bags = {}

for line in fileContents:
    # array of words
    halves = line.strip().split("contain")
    bagName = halves[0].replace(' ', '')[:-4]
    bagContents = halves[1].strip().split(', ')
    cDict = {}
    for content in bagContents:
        content = content.strip().replace('.', '')
        if content != "no other bags":
            contentArray = content.strip().split(' ')
            contentQuantity = contentArray[0]
            contentName = contentArray[1] + contentArray[2]
            cDict[contentName] = contentQuantity
    Bags[bagName] = cDict

parents = []

def parentSearch(parent, bag):
    global parents
    # print("Searching: ", parent)
    children = [c for c in Bags[parent].keys()]
    #print("Children: ", children)
    if children:
        for child in children:
            # print("      Checking child: ", child)
            if child == bag:
                # print("             Match! ")
                return True
            else:
                # print("             No match, calling parentSearch on ", child)
                if parentSearch(child, bag):
                    return True
    else:
        return False

def checkBag(bag):  
    for parent in Bags:
        if parentSearch(parent, bag):
            parents.append(parent)

    print(len(parents))
    
    
checkBag("shinygold")
# print("Elapsed time: ", time.time() - STARTTIME)