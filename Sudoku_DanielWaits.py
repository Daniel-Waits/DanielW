board = [
    [5,3,0,0,7,0,0,0,0],
    [6,0,0,1,9,5,0,0,0],
    [0,9,8,0,0,0,0,6,0],
    [8,0,0,0,6,0,0,0,3],
    [4,0,0,8,0,3,0,0,1],
    [7,0,0,0,2,0,0,0,6],
    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,5],
    [0,0,0,0,8,0,0,7,9],
    ]

def printBoard(board):
    print("")
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
                print("----------------------- ")
        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")
    print("")

def findNextEmpty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)

def isValid(board, curNumber, curPosition):
    ##check if number is in current row
    for i in range(len(board)):
        if curNumber == board[i][curPosition[1]] and curPosition[0] != i:
            return False

    ##check if number is in current column
    for i in range(len(board[0])):
        if curNumber == board[curPosition[0]][i] and curPosition[1] != i:
            return False

    ##check if number is in current 3x3 square
    x_square_coord = curPosition[1] // 3##is either 0, 1, 2 
    y_square_coord = curPosition[0] // 3##is either 0, 1, 2 
    for i in range(y_square_coord*3,y_square_coord*3 + 3):
        for j in range(x_square_coord*3,x_square_coord*3 + 3):
            if curNumber == board[i][j] and (i,j) != curPosition:
                return False
    return True

def solve(board):
    if solveRecursive(board):
        print("")
        print("SOLVED SUDOKU BOARD:")
        printBoard(board)
    else:
        return False

def solveRecursive(board):
    ##if true is returned at any point, the board is solved successfully
    findEmpty = findNextEmpty(board)
    if not findEmpty:
        return True #board solved
    else:
        x, y = findEmpty

    for i in range(1,10):
        if isValid(board, i, (x, y)):
            board[x][y] = i
        
            if solve(board):
                return True
            
            board[x][y] = 0
    return False
     
printBoard(board)
solve(board)
