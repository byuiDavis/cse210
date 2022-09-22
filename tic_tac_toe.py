#Carissa Davis


def main():
    print("Welcome to Tic Tac Toe! X will go first, and then O will go after")
    player = next_player("")
    board = make_board()
    while not (game_win(board) or game_draw(board)):
        display_board(board)
        player_turn(player, board)
        player = next_player(player)
    display_board(board)
    print("You won! Good game!") 

def make_board():
    #makes the tic tac toe board
    board = []
    for square in range(9):
        board.append(square + 1)
    return board

def display_board(board):
    #shows the board to the player
    print()
    print(f"{board[0]}|{board[1]}|{board[2]}")
    print('-----')
    print(f"{board[3]}|{board[4]}|{board[5]}")
    print('-----')
    print(f"{board[6]}|{board[7]}|{board[8]}")
    print()

def game_draw(board):
    #when the game is a draw
    for square in range(9):
        if board[square] != "x" and board[square] != "o":
            return False
    return True 

def game_win(board):
    #when someone wins the game
    return (board[0] == board[1] == board[2] or
            board[3] == board[4] == board[5] or
            board[6] == board[7] == board[8] or
            board[0] == board[3] == board[6] or
            board[1] == board[4] == board[7] or
            board[2] == board[5] == board[8] or
            board[0] == board[4] == board[8] or
            board[2] == board[4] == board[6])

def player_turn(player, board):
    #the players turn
    square = int(input(f"{player} Which spot would you like to mark? Choose between 1-9  "))
    board[square - 1] = player

def next_player(current):
    #changes the player
    if current == "" or current == "o":
        return "x"
    elif current == "x":
        return "o"

if __name__ == "__main__":
    main()