#1204

import time
import re

startTime = time.time()


#read drawn numbers file, get into useable format
file = open('./2021/1204/numbers.txt', 'r')
drawnNumbers = [num.strip() for num in file.read().split(',')]
file.close()

#readings the boards in to a dictionary
file = open('./2021/1204/boards.txt', 'r')
boardnumber = 0
boards = dict()
board = []
for line in file.readlines():
    if line != '\n':
        board.append(re.split('\s+', line.strip()))
    else:
        boards[boardnumber] = board.copy()
        boardnumber+=1
        board.clear()
file.close()


#checkboard to see if winner 
def checkIfBoardWinner(b):
    coltest = False
    rowtest = False

    #check if row is empty
    row = 0
    while row in range(len(boards[b])) and rowtest == False:
        rowtest = len(set(boards[b][row])) == 1
        row+=1

    #check if column is empty
    row = 0
    col = 0

    while col in range(len(boards[b][0])) and coltest == False:
        values = set(ele[col] for ele in boards[b])
        coltest = len(values) == 1
        col+=1


    if not rowtest and not coltest:
        return False
    else: 
        return True

def findNumberInBoard(board,drawnNum):
    #loop through each row of board
    for row in boards[board]:
        row[:] = [v if v != drawnNum else '' for v in row]
    return True

def calulateScore(b):

      
    sum = 0
    for row in boards[b]: #loop through rows
        for col in row:   #loop thru values in row adding non-blanks
            if col !='':
                sum+=int(col)
    return sum


#loop through drawn numbers while not board is a winning board
i = 0
b = 0
winningBoards = []
winingDraws = []
while i in range(len(drawnNumbers)):
    while b in range(len(boards)):
        if b not in winningBoards:
            findNumberInBoard(b,drawnNumbers[i]) #remove occurances of drawn number
            if checkIfBoardWinner(b):
                winningBoards.append(b)
                winingDraws.append(drawnNumbers[i])
        b+=1
    b=0
    i+=1

print("First winning board: " + str(winningBoards[0]) + " with a score of " + str((calulateScore(winningBoards[0])*int(winingDraws[0]))))

print("Last winning board: " + str(winningBoards[-1]) + " with a score of " + str((calulateScore(winningBoards[-1])*int(winingDraws[-1]))))
    
print("Total time: %s milliseconds" % round((time.time() - startTime)*1000, 3))
