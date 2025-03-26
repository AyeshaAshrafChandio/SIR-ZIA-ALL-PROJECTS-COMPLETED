import random

def print_board(board):
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("-----------")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("-----------")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")

def check_winner(board):
    # All possible winning combinations
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

def get_empty_positions(board):
    return [i for i, spot in enumerate(board) if spot == " "]

def minimax(board, depth, is_maximizing):
    winner = check_winner(board)
    
    if winner == "O":  # AI wins
        return 1
    elif winner == "X":  # Human wins
        return -1
    elif is_board_full(board):  # Tie
        return 0
    
    if is_maximizing:
        best_score = -float('inf')
        for position in get_empty_positions(board):
            board[position] = "O"
            score = minimax(board, depth+1, False)
            board[position] = " "
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for position in get_empty_positions(board):
            board[position] = "X"
            score = minimax(board, depth+1, True)
            board[position] = " "
            best_score = min(score, best_score)
        return best_score

def ai_move(board):
    best_score = -float('inf')
    best_move = None
    
    for position in get_empty_positions(board):
        board[position] = "O"
        score = minimax(board, 0, False)
        board[position] = " "
        
        if score > best_score:
            best_score = score
            best_move = position
    
    return best_move

def play_game():
    board = [" "] * 9
    print("Welcome to Tic-Tac-Toe vs AI!")
    print("Positions are numbered 1-9 (left to right, top to bottom)")
    
    while True:
        print_board(board)
        
        # Human move
        while True:
            try:
                position = int(input("Your move (1-9): ")) - 1
                if position in range(9) and board[position] == " ":
                    break
                print("Invalid move! Try again.")
            except ValueError:
                print("Please enter a number 1-9!")
        
        board[position] = "X"
        
        # Check if human won
        if check_winner(board) == "X":
            print_board(board)
            print("You win! Impossible! 🤯")
            break
            
        if is_board_full(board):
            print_board(board)
            print("It's a tie! 😐")
            break
            
        # AI move
        print("AI is thinking...")
        ai_position = ai_move(board)
        board[ai_position] = "O"
        
        # Check if AI won
        if check_winner(board) == "O":
            print_board(board)
            print("AI wins! Better luck next time! 😎")
            break
            
        if is_board_full(board):
            print_board(board)
            print("It's a tie! 😐")
            break

# Start the game
play_game()