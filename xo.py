# Initialize the board
board = [" " for _ in range(9)]

# Function to print the board
def print_board():
    row1 = "|".join(board[0:3])
    row2 = "|".join(board[3:6])
    row3 = "|".join(board[6:9])
    print(row1)
    print("-----")
    print(row2)
    print("-----")
    print(row3)

# Function to check for a winning condition
def check_win(player):
    # Check rows
    for i in range(0, 9, 3):
        if board[i] == board[i + 1] == board[i + 2] == player:
            return True
    # Check columns
    for i in range(3):
        if board[i] == board[i + 3] == board[i + 6] == player:
            return True
    # Check diagonals
    if board[0] == board[4] == board[8] == player:
        return True
    if board[2] == board[4] == board[6] == player:
        return True
    return False

# Function to play the game
def play_game():
    currentPlayer = "X"
    game_over = False

    while not game_over:
        print_board()
        print(f"It's {currentPlayer}'s turn. Enter a position from 1-9: ")
        position = int(input()) - 1

        if board[position] == " ":
            board[position] = currentPlayer

            if check_win(currentPlayer):
                print(f"{currentPlayer} wins!")
                game_over = True
            elif " " not in board:
                print("It's a tie!")
                game_over = True
            else:
                currentPlayer = "O" if currentPlayer == "X" else "X"
        else:
            print("That position is already filled. Try again.")

# Start the game
play_game()