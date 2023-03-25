board = [["_","_","_"], ["_","_","_"], ["_","_","_"]]
player_x = "X" # player_x is 'x' which plays first always
player_o = "O" # player_o is '0'

def print_board(board): # it displays a board with lines
    for row in board:
        print(row)

def check_win(board, player): # it checks where there is same continuosly for three boxes either horizontally ,vertically, diagonally
    # check rows
    for row in board:
        if row == [player, player, player]:
            return True
    # check columns
    for i in range(3):
        if board[0][i] == player and board[1][i] == player and board[2][i] == player:
            return True
    # check diagonals
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    return False

def check_tie(board): # if all chances are done and no one win then is is a tie
    for row in board:
        if "_" in row:
            return False
    return True

def start_game(): # the player choose a numbers 0-2 (row,col) and start the game
    current_player = player_x
    while True:
        print_board(board)
        row = int(input(f"{current_player}, choose row (0-2): "))
        col = int(input(f"{current_player}, choose col (0-2): "))
        if row not in range(3) or col not in range(3): # it checks the range between 0-2 and if it is bigger or lower then
            print("Invalid input. Please choose a number between 0 and 2.")
            continue

        if board[row][col] != "_": #when you choose the same numbers (row,col) it will give a massage
            print("This slot is already taken. Please choose another one.")
            continue
        board[row][col] = current_player
        if check_win(board, current_player): #when you win it will give massage
            print_board(board)
            print(f"Congratulations! {current_player} wins!")
            break
        elif check_tie(board): # when it is a tie it will give a massage
            print_board(board)
            print("It's a tie!")
            break
        current_player = player_o if current_player == player_x else player_x

#reset board
def clear_board():
    for row in board:
        for i in range(3):
            row[i]= "_"




#after you finish the game you can play again if you want
play_again = True

while play_again:
    clear_board()
    start_game()
    if input('Do yoy want to play again y/n:  ').upper() != 'Y':
        play_again=False

