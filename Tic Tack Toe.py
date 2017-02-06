

def main():
    #Program Goal: Create command line version of Tic Tack Toe, with two  players taking turns.

    print("Welcome to Tic Tack Toe!")
    print("Rules: Two players take turns placing X's and O's in spaces on a 9x9 board.")
    print("Whichever player manages to get three X's or three O's in a row, wins!") 
    print("Enter values between 0,1,and 2 to designate your rows and collumns")

    mark=0
    board = [["*","*","*"],["*","*","*"],["*","*","*"]]
    turnCount=0
    gameState=False
    won=1
    row=0
    col=0


    while turnCount<9 and gameState==False:
        printBoard(board)
        if turnCount%2==0:
            #player2
            mark="O"
            print("Player 1, make your move:")
            #makeMove()
        else:
            #player1
            mark="X"
            print("Player 2, make your move:")
            #makeMove()
        (row,col)=makeMove()
        if board[row][col]!="*":
            print("Someone's already gone there!")
            (row,col)=makeMove()
        board[row][col]=mark
        turnCount+=1
        #if row in board == ["X","X","X"]or["O","O","O"]:
            #ameState=True  (This is evicence of a long and drawn out attempt at the last part of the A program) 
    


def printBoard(board):
    for row in board:
        for item in row:
            print (" "+str(item)+" ", end=" ")
        print()

def makeMove():
    row=int(input("What row will you place your mark in?"))
    col=int(input("What collumn will you place your mark in?"))
    if row and col <0 or row and col>2:
        print("Values not on board")
        print("Try again!")
        makeMove()
    return (row, col)
main()

