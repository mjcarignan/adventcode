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
    print(b, boards[b])
    row = 0
    while row in range(len(boards[b])) and rowtest == False:
        rowtest = len(set(boards[b][row])) == 1
        row+=1

    #check if column is empty
    row = 0
    col = 0

    # test = ''
    # while col in range(len(boards[b][0])) and coltest == False:
    #     test = ''
    #     while row in range(len(boards[b])):
    #         test += boards[b][row][col]
    #         row+=1
    #     coltest = test == ''
    #     col+=1

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
    #loop through rows
        #loop thru values in row adding non-blanks
    sum = 0
    for row in boards[b]:
        for col in row:
            if col !='':
                sum+=int(col)
    return sum


#loop through drawn numbers while not board is a winning board
i = 0
b = 0
winner = False
numWinningBoard = int()
drawnNum = int()
winningBoards = []
while i in range(len(drawnNumbers)) and winner == False:
    drawnNum = drawnNumbers[i] #find drawnnumber in each board
    print(drawnNum)
    while b in range(len(boards)) and winner == False:
        findNumberInBoard(b,drawnNum) #remove occurances of drawn number
        winner = checkIfBoardWinner(b) # check if the board is a winner
        if winner:
            numWinningBoard = b
        b+=1
    b=0
    i+=1
print()
print(calulateScore(numWinningBoard))
print(drawnNum)
print("Winning board: " + str(numWinningBoard) + " with a score of " + str((calulateScore(numWinningBoard)*int(drawnNum))))

    

