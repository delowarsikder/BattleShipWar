# https://github.com/gbrough/battleship/blob/main/5_ship_types_with_computer.py

'''
  Legend:
    1. "." = water or empty space
    2. "O" = part of ship
    3. "X" = part of ship that was hit with bullet
    4. "*" = water that was shot with bullet, a miss because it hit no ship
'''

import time
import random

BOARD_SIZE = 9
# LENGTH_OF_SHIPS = [2,3,5,4]
# ##Define the maximum length of ship
MAX_SHIP_LENGHT = 5
NUMBER_OF_SHIP = 2

totalShipLength=0

# Boad already created
# player own board
PLAYER_BOARD = [["."] * BOARD_SIZE for i in range(BOARD_SIZE)]
# AI agent own board
COMPUTER_BOARD = [["."] * BOARD_SIZE for i in range(BOARD_SIZE)]
# both invisible to each other
# AI board that guess by player
PLAYER_GUESS_BOARD = [["."] * BOARD_SIZE for i in range(BOARD_SIZE)]
# Player Board that guess by AI
COMPUTER_GUESS_BOARD = [["."] * BOARD_SIZE for i in range(BOARD_SIZE)]
LETTER = "ABCDEFGHI"

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
            if board[startRow][i] == "O":
                return True
    elif orientation=="V":
        for i in range(startRow, startRow + shipLength):
            if board[i][startColumn] == "O":
                return True
    return False

# userShip placement
def userShipPlacement():
    while True:
        try:
            shipOrientation = input("Enter orientation (H or V): ").upper()
            if shipOrientation == "H" or shipOrientation == "V":
                break
            else:
                print('Wrong!!! Again...',end='')
        except KeyError:
            print('Again!!! Enter a valid orientation H or V')
    while True:
        try:
            startRow = int(input("Enter the row 1-9 of the ship start: "))
            startRow=startRow-1
            if(0<startRow<BOARD_SIZE):
                break
            else:
                print('Wrong!!! Again...',end='')
        except ValueError:
            print('Again!!! Enter a valid row number between 1-9')
    while True:
        try:
            column = input(
                "Enter the column (A-I) of the ship start: ").upper()
            if column in LETTER:
                startColumn=int(ord(column)-ord('A'))
                break
            else:
                print('Wrong!!! Again...',end='')
        except KeyError:
            print('Again!!! Enter a valid letter between A-H')
    return startRow, startColumn, shipOrientation


# Place the ship in the ocean
def shipPlacement(board):
    global totalShipLength
    # loop through length of ships
    random.seed(time.time())
    for numberOfShip in range(NUMBER_OF_SHIP):
        # loop until ship fits and doesn't overlap
        shipLength = random.randint(MAX_SHIP_LENGHT-3, MAX_SHIP_LENGHT)
        totalShipLength=totalShipLength+shipLength
        while True:
            if board==COMPUTER_BOARD:
                shipOrientation = random.choice(["H", "V"])
                startRow = random.randint(0, BOARD_SIZE-1)
                startColumn = random.randint(0, BOARD_SIZE-1)
                # check the ship fit or not
                if (checkFitTheShip(shipLength, startRow, startColumn, shipOrientation)):
                    # check if ship overlaps
                    if (checkShipOverlaping(board, shipLength, startRow, startColumn, shipOrientation) == False):
                        # place ship
                        if shipOrientation == "H":
                            for i in range(startColumn, startColumn + shipLength):
                                board[startRow][i] = "O"
                        else:
                            for i in range(startRow, startRow + shipLength):
                                board[i][startColumn] = "O"
                        break
            
            elif board==PLAYER_BOARD:
                print("Your current ship lenght is: ",shipLength)
                # while True:
                    # print("Enter the length of Ship ",str(numberOfShip+1),"between (2-5): ",end='')
                    # shipLength = int(input())
                    # if(shipLength < MAX_SHIP_LENGHT):
                    #     break
                    # else:
                    #     print('Wrong!!! Again...',end='')
                startRow, startColumn, orientation = userShipPlacement()  # get input from user with validation
                startRow=int(startRow)
                startColumn=int(startColumn)

                if (checkFitTheShip(shipLength, startRow, startColumn, orientation)):

                    # print("ship fit into the board")
                    # check if ship overlaps
                    if (checkShipOverlaping(board, startRow, startColumn, orientation, shipLength) == False):
                            # place ship
                        if (orientation == "H"):
                            for i in range(startColumn, startColumn + shipLength):
                                board[startRow][i] = "O"
                        elif (orientation=="V"):
                            for i in range(startRow, startRow + shipLength):
                                board[i][startColumn] = "O"

                        print_board(PLAYER_BOARD)
                        break
                    else:
                        print("Your new ship is overlaped to ther ship !!!")
                        print("Please Enter Valid posion")
                else:
                    print("Your Ship shape out of range")
                    print("Please Enter Valid posion")



###get input from user where he shoot
##search the location where shot for attacking the ai
def userShootingPosion():
    while True:
        try:
            startRow = int(input("Enter the row 1-9 of the ship start: "))
            startRow=startRow-1
            if(0<=startRow<BOARD_SIZE):
                break
            else:
                print('Wrong!!! Again...',end='')
        except ValueError:
            print('Again!!! Enter a valid row number between 1-9')
    while True:
        try:
            column = input(
                "Enter the column (A-I) of the ship start: ").upper()
            if column in LETTER:
                startColumn=int(ord(column)-ord('A'))
                break
            else:
                print('Wrong!!! Again...',end='')
        except KeyError:
            print('Again!!! Enter a valid letter between A-H')
    return startRow, startColumn

###counter check who is alive Human or AI
def sinkBoatCounter(board):
    counter=0
    for row in board:
        for col in board[row]:
            if(board[row][col]=="X"):
                counter=counter+1
    return counter


###shoot the board
def shootTheBoard(board):
    if (board==PLAYER_GUESS_BOARD):
        hitRow,hitColumn=userShootingPosion()
        if(COMPUTER_BOARD[hitRow][hitColumn]=="0"):
            PLAYER_GUESS_BOARD[hitRow][hitColumn]="X"
        else:
            PLAYER_GUESS_BOARD[hitRow][hitColumn]="*"
    elif (board==COMPUTER_GUESS_BOARD):
        hitRow=random.randint(0, BOARD_SIZE-1)
        hitColumn=random.randint(0, BOARD_SIZE-1)

        if(PLAYER_BOARD[hitRow][hitColumn]=="0"):
            PLAYER_BOARD[hitRow][hitColumn]="X"
            COMPUTER_GUESS_BOARD[hitRow][hitColumn]="X"
        else:
            PLAYER_BOARD[hitRow][hitColumn]="*"
            COMPUTER_GUESS_BOARD[hitRow][hitColumn]="*"

def main():
    print("Computer")
    shipPlacement(COMPUTER_BOARD)
    print_board(COMPUTER_BOARD)

    shipPlacement(PLAYER_BOARD)

    aiAgentAlive=True
    humanAgentAlive=True
    humanAgentTurn=True
    aiAgentTrun=True

    while aiAgentAlive and humanAgentAlive:
        while humanAgentTurn:
            print_board(PLAYER_GUESS_BOARD)
            print("Guess the Agent ship:")
            shootTheBoard(PLAYER_GUESS_BOARD)
            print_board(PLAYER_GUESS_BOARD)
            humanAgentTurn=False
            aiAgentTrun=True
        ###computer board that player guess
        if numberOfShinkBoard(PLAYER_GUESS_BOARD)==totalShipLength:
            print("Congratulation!!!,You have won the Game")
            aiAgentAlive=False

        while aiAgentAlive:
            shootTheBoard(COMPUTER_GUESS_BOARD)
            print_board(PLAYER_BOARD)
            aiAgentTrun=False
            humanAgentTurn=True

        ##human board -that Computer Guess
        if numberOfShinkBoard(COMPUTER_GUESS_BOARD)==totalShipLength:
            print("Sorry!!!,You have loss the Game")
            humanAgentAlive=False   



if __name__ == '__main__':
    main()
