# Simple Tic-Tac-Toe Game
def print_board(board):
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("-----------")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("-----------")
    print(f" {board[6]} | {board[7]} | {board[8]} ")

def check_winner(board):
    # Check all possible winning combinations
    wins = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]              # diagonals
    ]
    
    for combo in wins:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != " ":
            return board[combo[0]]
    return None

def is_board_full(board):
    return " " not in board

def play_game():
    board = [" "] * 9
    current_player = "X"
    
    print("Welcome to Tic-Tac-Toe!")
    print("Enter positions (1-9) as shown below:")
    print(" 1 | 2 | 3 ")
    print("-----------")
    print(" 4 | 5 | 6 ")
    print("-----------")
    print(" 7 | 8 | 9 ")
    print("\nLet's begin!\n")
    
    while True:
        print_board(board)
        position = input(f"Player {current_player}'s turn (1-9): ")
        
        # Validate input
        if not position.isdigit() or int(position) < 1 or int(position) > 9:
            print("Please enter a number between 1-9")
            continue
            
        position = int(position) - 1  # Convert to 0-based index
        
        if board[position] != " ":
            print("That position is already taken!")
            continue
            
        board[position] = current_player
        
        # Check for winner
        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"Player {winner} wins! 🎉")
            break
            
        # Check for tie
        if is_board_full(board):
            print_board(board)
            print("It's a tie! 🤝")
            break
            
        # Switch players
        current_player = "O" if current_player == "X" else "X"

# Start the game
play_game()