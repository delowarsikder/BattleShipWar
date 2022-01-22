import time
import random
BOARD_SIZE = 9
ALL_SHIPS = []
# ##Define the maximum length of ship
MAX_SHIP_LENGHT = 6
NUMBER_OF_SHIP = 5

totalShipLength = 0

# symbol
boatSymbol = "@"
waterSymbol = "~"
hitShootSymbol = "X"
missShootSymbol = "#"

# Boad already created
# player own board
HUMAN_BOARD = [[waterSymbol] * BOARD_SIZE for i in range(BOARD_SIZE)]
# AI agent own board
AI_BOARD = [[waterSymbol] * BOARD_SIZE for i in range(BOARD_SIZE)]
# both invisible to each other
# AI board that guess by player
HUMAN_GUESS_BOARD = [[waterSymbol] * BOARD_SIZE for i in range(BOARD_SIZE)]
# Player Board that guess by AI
AI_GUESS_BOARD = [[waterSymbol] * BOARD_SIZE for i in range(BOARD_SIZE)]
LETTER = "ABCDEFGHIJ"

# print the grid of board


def print_board(board):
    print("  ", end='')
    for i in range(BOARD_SIZE):
        print(LETTER[i], end=' ')
    print('')
    print("  ", end='')
    for i in range(BOARD_SIZE):
        print('+-', end='')
    print('')
    row_number = 1
    for row in board:
        print("%d|%s|" % (row_number, "|".join(row)))
        row_number += 1


# check if ship fits in board
def checkFitTheShip(shipLength, startRow, startColumn, orientation):
    if orientation == "H":
        if startColumn + shipLength > BOARD_SIZE:
            return False
        else:
            return True

    elif orientation == "V":

        if startRow + shipLength > BOARD_SIZE:
            return False
        else:
            return True

# check ship is overlap or not when place the ship


def checkShipOverlaping(board, shipLength, startRow, startColumn, orientation):

    if orientation == "H":

        for i in range(startColumn, startColumn + shipLength):
            if board[startRow][i] == boatSymbol:
                return False

    elif orientation == "V":

        for i in range(startRow, startRow + shipLength):
            if board[i][startColumn] == boatSymbol:
                return False
    return True

# userShip placement


def userShipPlacement():
    while True:
        try:
            shipOrientation = input("Enter orientation (H or V): ").upper()
            if (shipOrientation == "H" or shipOrientation == "V"):
                break
            else:
                print('Wrong!!! Again...', end='')
        except KeyError:
            print('Again!!! Enter a valid orientation H or V')
    while True:
        try:
            print("Enter the row 1-"+str(BOARD_SIZE) +
                  " of the ship start: ", end='')
            startRow = int(input())
            startRow = startRow-1
            if(-1 < startRow < BOARD_SIZE):
                break
            else:
                print('Wrong!!! Again...', end='')
        except ValueError:
            print("Again!!! Enter the row 1-"+str(BOARD_SIZE) +
                  " of the ship start: ", end='')
    while True:
        try:
            print('Enter the column (' +
                  LETTER[0]+'-'+LETTER[BOARD_SIZE-1]+') of the ship start: ', end='')
            column = input().upper()
            if column in LETTER:
                startColumn = int(ord(column)-ord('A'))
                break
            else:
                print('Wrong!!! Again...', end='')
        except KeyError:
            print('Again!!! Enter the column (' +
                  LETTER[0]+'-'+LETTER[BOARD_SIZE-1]+') of the ship start: ')
    return startRow, startColumn, shipOrientation

# create a ship with ship length


def createShipLength():
    global totalShipLength, ALL_SHIPS
    for i in range(NUMBER_OF_SHIP):
        lengthOfShip = random.randint(MAX_SHIP_LENGHT-3, MAX_SHIP_LENGHT)
        ALL_SHIPS.append(lengthOfShip)
        totalShipLength = totalShipLength+lengthOfShip

# Place the ship in the ocean


def shipPlacement(board):
    global totalShipLength
    # loop through length of ships
    random.seed(time.time())
    for k in range(NUMBER_OF_SHIP):
        shipLength = ALL_SHIPS[k]
        # loop until ship fits and doesn't overlap
        while True:
            if (board == AI_BOARD):
                shipOrientation = random.choice(["H", "V"])
                startRow = random.randint(0, BOARD_SIZE-1)
                startColumn = random.randint(0, BOARD_SIZE-1)
                # check the ship fit or not
                if (checkFitTheShip(shipLength, startRow, startColumn, shipOrientation)):
                    # check if ship overlaps
                    if (checkShipOverlaping(board, shipLength, startRow, startColumn, shipOrientation)):
                        # place ship
                        if shipOrientation == "H":
                            for i in range(startColumn, startColumn + shipLength):
                                board[startRow][i] = boatSymbol
                        else:
                            for i in range(startRow, startRow + shipLength):
                                board[i][startColumn] = boatSymbol
                        break

            elif (board == HUMAN_BOARD):
                ###randomly generate
                shipOrientation = random.choice(["H", "V"])
                startRow = random.randint(0, BOARD_SIZE-1)
                startColumn = random.randint(0, BOARD_SIZE-1)
                # check the ship fit or not
                if (checkFitTheShip(shipLength, startRow, startColumn, shipOrientation)):
                    # check if ship overlaps
                    if (checkShipOverlaping(board, shipLength, startRow, startColumn, shipOrientation)):
                        # place ship
                        if shipOrientation == "H":
                            for i in range(startColumn, startColumn + shipLength):
                                board[startRow][i] = boatSymbol
                        else:
                            for i in range(startRow, startRow + shipLength):
                                board[i][startColumn] = boatSymbol
                        break

'''
                print("Your current ship lenght is: ", shipLength)
                # get input from user with validation
                startRow, startColumn, orientation = userShipPlacement()
                startRow = int(startRow)
                startColumn = int(startColumn)

                if (checkFitTheShip(shipLength, startRow, startColumn, orientation)):

                    # check if ship overlaps
                    if (checkShipOverlaping(board, shipLength, startRow, startColumn, orientation)):
                            # place ship
                        if (orientation == "H"):
                            for i in range(startColumn, startColumn + shipLength):
                                board[startRow][i] = boatSymbol
                        elif (orientation == "V"):
                            for i in range(startRow, startRow + shipLength):
                                board[i][startColumn] = boatSymbol

                        print_board(HUMAN_BOARD)
                        break
                    else:
                        print("Your new ship is overlaped to other ship !!!")
                        print("Please Enter Valid posion")
                else:
                    print("Your Ship shape out of range")
                    print("Please Enter Valid posion")

'''

# get input from user where he shoot
# search the location where shoot for attacking the ai
def userShootingPosion():
    while True:
        try:
            print("Enter the row 1-"+str(BOARD_SIZE) +
                  " of the ship start: ", end='')
            startRow = int(input())
            startRow = startRow-1
            if(0 <= startRow < BOARD_SIZE):
                break
            else:
                print('Wrong!!! Again...', end='')
        except ValueError:
            print("Again!!! Enter the row 1-" +
                  str(BOARD_SIZE)+"of the ship start: ", end='')
    while True:
        try:
            print('Enter the column (' +
                  LETTER[0]+'-'+LETTER[BOARD_SIZE-1]+') of the ship start: ', end='')
            column = input().upper()
            if column in LETTER:
                startColumn = int(ord(column)-ord('A'))
                break
            else:
                print('Wrong!!! Again...', end='')
        except KeyError:
            print('Again!!! Enter the column (' +
                  LETTER[0]+'-'+LETTER[BOARD_SIZE-1]+') of the ship start: ')
    return startRow, startColumn

# counter check who is alive Human or AI


def sinkBoatCounter(board):
    counter = 0
    for row in board:
        for col in row:
            if(col == hitShootSymbol):
                counter = counter+1
    return counter

aiFirstHitShoot=False
aiSuccessFullHit=[]
# shoot the board
def shotTheBoard(board):
    global aiFirstHitShoot,aiSuccessFullHit
    if (board == HUMAN_GUESS_BOARD):
        hitRow, hitColumn = userShootingPosion()
        if(AI_BOARD[hitRow][hitColumn] == boatSymbol):
            print("Human Success full hit: ",hitRow," ",hitColumn)
            HUMAN_GUESS_BOARD[hitRow][hitColumn] = hitShootSymbol
        else:
            print("Human Miss hit")
            HUMAN_GUESS_BOARD[hitRow][hitColumn] = missShootSymbol

    elif (board == AI_GUESS_BOARD):
        hitRow = -1
        hitColumn = -1
        if aiFirstHitShoot == False:
            while True:
                hitRow = random.randint(0, BOARD_SIZE-1)
                hitColumn = random.randint(0, BOARD_SIZE-1)
                if (AI_GUESS_BOARD[hitRow][hitColumn]==waterSymbol):
                    break
            print('EIJEEEE EIJEEEEE EIJEEEEE')
        else:
            dx = [1,-1,0,0]
            dy = [0,0,1,-1]
            print("Ai Successfull hit",aiSuccessFullHit)
            flag = False
            for x in range(0,len(aiSuccessFullHit)):
                for i in range(0,4):
                    hitRow = aiSuccessFullHit[x][0] + dx[i]
                    hitColumn = aiSuccessFullHit[x][1]+ dy[i]
                    if (hitRow>=0 and hitRow<9 and hitColumn>=0 and hitColumn<9):
                        #nothing
                        pass
                    else:
                        continue
                        
                    if AI_GUESS_BOARD[hitRow][hitColumn] == hitShootSymbol or AI_GUESS_BOARD[hitRow][hitColumn] == missShootSymbol:
                        continue 
                    if(HUMAN_BOARD[hitRow][hitColumn] == boatSymbol):
                        flag = True
                        break
                if flag==True:
                    break
        
            if flag == False:
                print('NO MAMU NOOOOOOOO')
                aiSuccessFullHit = []
                while True:
                    hitRow = random.randint(0, BOARD_SIZE-1)
                    hitColumn = random.randint(0, BOARD_SIZE-1)
                    if (AI_GUESS_BOARD[hitRow][hitColumn]==waterSymbol):
                        break
        
            
            

        if(HUMAN_BOARD[hitRow][hitColumn] == boatSymbol):
            if aiFirstHitShoot == False:
                aiFirstHitShoot=True
            HUMAN_BOARD[hitRow][hitColumn] = hitShootSymbol
            AI_GUESS_BOARD[hitRow][hitColumn] = hitShootSymbol
            aiSuccessFullHit.append([hitRow,hitColumn])
            print("AI Sucessfull hit: ",hitRow," ",hitColumn)
        else:
            HUMAN_BOARD[hitRow][hitColumn] = missShootSymbol
            AI_GUESS_BOARD[hitRow][hitColumn] = missShootSymbol
            print("Ai miss hit: ",hitRow," ",hitColumn)

def main():
    # this function randomly creat a ship length
    createShipLength()

    print("AI Board")
    shipPlacement(AI_BOARD)
    print_board(AI_BOARD)

    # print("\n\nYour Sample Board")
    shipPlacement(HUMAN_BOARD)
    print("\n Your Board After Ship placement")
    print_board(HUMAN_BOARD)
    
    aiAgentAlive = True
    humanAgentAlive = True
    humanAgentTurn = True
    aiAgentTurn = True

    while(aiAgentAlive and humanAgentAlive):
        while (humanAgentTurn):
            print("AI Board where you shoot")
            print_board(HUMAN_GUESS_BOARD)
            print("Guess the AI ship in Board:")
            shotTheBoard(HUMAN_GUESS_BOARD)
            print_board(HUMAN_GUESS_BOARD)
            humanAgentTurn = False
            aiAgentTurn = True
        # computer board that player guess
        if (sinkBoatCounter(HUMAN_GUESS_BOARD) == totalShipLength):
            print("Congratulation!!!,You have won the Game")
            aiAgentAlive = False

        while (aiAgentTurn):
            shotTheBoard(AI_GUESS_BOARD)
            print("\n After AI shoot, Your board situation:")
            print_board(HUMAN_BOARD)
            aiAgentTurn = False
            humanAgentTurn = True

        # human board -that Computer Guess
        if (sinkBoatCounter(AI_GUESS_BOARD) == totalShipLength):
            print("Sorry!!!,You have loss the Game")
            humanAgentAlive = False


if __name__ == '__main__':
    main()
