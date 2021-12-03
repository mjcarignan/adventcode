#1208-2020

import time
import re

startTime = time.time()

#read file, get into useable format
file = open('./2020/20201208_data_sample.txt', 'r')
instructions = [re.split('\s', nav.strip()) for nav in file.readlines()]
file.close()

#part 1
accumulator = 0
i = 0
exedInstructions = list()
while i <= (len(instructions)) and i not in exedInstructions:
    exedInstructions.append(i)
    match instructions[i][0]:
        case "acc":
            accumulator+=int(instructions[i][1])
            i+=1
        case "jmp":
            i +=int(instructions[i][1])
        case "nop":
            i +=1
print("Part 1: " + str(accumulator))


#part 2

# #Tests is an instruction will lead to a repeat of instructions
# def testRepeat (x):
#     inst = list()
#     while x <= (len(instructions)) and x not in inst:
#         inst.append(x)
#         match instructions[x][0]:
#             case "acc":
#                 x+=1
#             case "jmp":
#                 x +=int(instructions[i][1])
#             case "nop":
#                 x +=1
#     if x in inst:
#         return True
#     else: 
#         return False



accumulator = 0
i = 0
exedInstructions = list()
# while i <= (len(instructions)) and i not in exedInstructions:
#     exedInstructions.append(i)
#     match instructions[i][0]:
#         case "acc":
#             accumulator+=int(instructions[i][1])
#             i+=1
#         case "jmp":
#             if testRepeat(i) == True:
#                 i+=1
#             else: 
#                 i+=int(instructions[i][1])
#         case "nop":
#             if testRepeat(i) == True:
#                 if int(instructions[i][1]) != 0:
#                     i+=int(instructions[i][1])
#                 else:
#                     i+=1
#             else: 
#                 i+=1
#     print(i)

print("Part 2: " + str(accumulator))

