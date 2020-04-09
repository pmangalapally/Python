theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
printBoard(theBoard)

#theBoard = {'top-L': 'O', 'top-M': 'O', 'top-R': 'O', 'mid-L': 'X', 'mid-M':
#'X', 'mid-R': ' ', 'low-L': ' ', 'low-M': ' ', 'low-R': 'X'}

#printBoard(theBoard)
theBoardRemaining = theBoard.copy()

turn = 'X'
for i in range(9):
    print(theBoard)
    print('Turn for ' + turn + '. Move on which space?')
    move = input('>')
    while move not in theBoardRemaining.keys():
        print("Enter valid input from the dictionary", theBoardRemaining)
        move = input('>')
    
    del theBoardRemaining[move]

    theBoard[move] = turn
    if turn == 'X':
         turn = 'O'
    else:
         turn = 'X'

printBoard(theBoard)
