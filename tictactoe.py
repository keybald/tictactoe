# Create an initial version of the board on which the game will be played

board_init = ['1','2','3','4','5','6','7','8','9'] 
victory = False

# Force player1 to select either 'X' or 'O'. If a different symbol is selected the game won't start

def ready_to_play():
    player1 = ''
    while(player1 != 'X' and player1 != 'O'):
        player1 = input("Player 1 please pick a marker 'X' or 'O': ")
    return player1

# A function to display the current state of the board that is kept in the board_init list

def display_board(board):
    print(board[0] + ' ' + board[1] + ' ' + board[2])
    print(board[3] + ' ' + board[4] + ' ' + board[5])
    print(board[6] + ' ' + board[7] + ' ' + board[8])

# This function places a symbol selected by one of the players onto the board_init list

def symbol_placer(player,number,board):
    counter = 0
    for i in board:
        if(i == str(number)):
            board_init[counter] = player
        counter += 1
    display_board(board)
    
# This function check all the possible arrangements of the symbols that lead to victory and compares those arrangements with the current state of the board_init 
# list. If the symbols are arranged, so to achieve the victory, the function returns True, and otherwise False. 
    
def victory_check(board,mark):
    if(
    (board[0] == mark and board[1] == mark and board[2] == mark)or
    (board[3] == mark and board[4] == mark and board[5] == mark)or
    (board[6] == mark and board[7] == mark and board[8] == mark)or
    (board[0] == mark and board[3] == mark and board[6] == mark)or
    (board[1] == mark and board[4] == mark and board[7] == mark)or
    (board[2] == mark and board[5] == mark and board[8] == mark)or
    (board[0] == mark and board[4] == mark and board[8] == mark)or
    (board[2] == mark and board[4] == mark and board[6] == mark)):
        return True
    else: 
        return False

# A simple function that returns True if the board_init is full and False if there are still digits present on the board
    
def table_full_check(board):
    for i in board:
        if(i.isdigit()):
            return False
    return True

# The main function that takes advantage of other functions in this listing

def play():
    player1 = ready_to_play()
    player2 = ''

    if(player1 == 'X'):
        player2 = 'O'
    else:
        player2 = 'X'
        
    display_board(board_init)
    
    while(victory != True):

# There is one bug that I discovered, namely, that the application returns the game over message only after all the fields are populated with either
# X or O, and then, the player still needs to type in one of the symbols once to generate the game over message. 

        if(table_full_check(board_init)):
            print("Nobody has won. Game over!")
            break
        player1_select = int(input("Player 1 please select a number to place the " + player1 + " symbol\n"))
        symbol_placer(player1,player1_select,board_init)
        if(victory_check(board_init,player1)):
            print("Player1: Victory!")
            break
        player2_select = int(input("Player 2 please select a number to place the " + player2 + " symbol\n"))
        symbol_placer(player2,player2_select,board_init)
        if(victory_check(board_init,player2)):
            print("Player2: Victory!")
            break
play()
