def display_board(board):

    display = [
        ["*********************"],
        [f"*  {board[0][0]}   |  {board[0][1]}  |  {board[0][2]}   *"],
        ["* ---- | --- |----- *"],
        [f"*  {board[1][0]}   |  {board[1][1]}  |  {board[1][2]}   *"],
        ["* ---- | --- |----- *"],
        [f"*  {board[2][0]}   |  {board[2][1]}  |  {board[2][2]}   *"],
        ["*********************"]
    ]

    for line in display:
         for item in line:
             print(item, end="")
         print()

board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]


def player_input(board, player):
    #get player moves
    while True:
       row = int(input(f"Player {player}, which row would you like go in? ")) -1
       col = int(input(f"Player {player}, which column would you like to go in? "))-1

       if 0 <= row <= 2 and 0 <= col <= 2 and board[row][col] == " ":
           board[row][col] = player
           break
       else:
          print("That position is already taken dummy!")


def check_winner(board, player):
    #check rows
    for row in board:
        if all(cell == player for cell in row):
            return True

    #check columns
    for col in range(3):
        if all(cell == player for cell in [board[row][col] for row in range(3)]):
            return True

    #check diagonals
    if all(cell == player for cell in [board[x][x] for x in range(3)]):
        return True    

    if all(cell == player for cell in [board[x][2-x] for x in range(3)]):
        return True

    return False

def check_tie(board):
    #check for tie
    for row in board:
        if " " in row:
            return False
    else:
        return True

def play():
    current_player = "X"

    while True:
        display_board(board)
        player_input(board, current_player)

        if check_winner(board, current_player):
            display_board(board)
            print(f"Player {current_player} wins! You are currently the best Tic Tac Toe player in the room!")
            break
        elif check_tie(board):
            display_board(board)
            print(f"You guys tied! (lame)")
            break

        if current_player == "X":
            current_player = "O"
        else:
           current_player = "X"

play()