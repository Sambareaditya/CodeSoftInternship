# Build a simple chatbot that responds to user inputs based on
# predefined rules. Use if-else statements or pattern matching
# techniques to identify user queries and provide appropriate
# responses. This will give you a basic understanding of natural language processing and conversation flow.
import random
PLAYER_X = 'X'  
PLAYER_O = 'O'  
EMPTY = ' '  

def print_board(board):
    print("\n")
    for i in range(3):
        print(" | ".join(board[i]))
        if i < 2:
            print("---------")
    print("\n")

def check_winner(board, player):
    for i in range(3):
        if all([board[i][j] == player for j in range(3)]) or \
           all([board[j][i] == player for j in range(3)]):
            return True
    if (board[0][0] == player and board[1][1] == player and board[2][2] == player) or \
       (board[0][2] == player and board[1][1] == player and board[2][0] == player):
        return True
    return False

def check_draw(board):
    return all([cell != EMPTY for row in board for cell in row])

def minimax(board, depth, is_maximizing_player):
    if check_winner(board, PLAYER_O):
        return 1  
    if check_winner(board, PLAYER_X):
        return -1  
    if check_draw(board):
        return 0
    
    if is_maximizing_player:
        best = -float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = PLAYER_O
                    best = max(best, minimax(board, depth + 1, False))
                    board[i][j] = EMPTY 
        return best
    else:
        best = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = PLAYER_X  
                    best = min(best, minimax(board, depth + 1, True))
                    board[i][j] = EMPTY  
        return best

def find_best_move(board):
    best_val = -float('inf')
    best_move = (-1, -1)
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                board[i][j] = PLAYER_O
                move_val = minimax(board, 0, False)
                board[i][j] = EMPTY  
                if move_val > best_val:
                    best_val = move_val
                    best_move = (i, j)
    return best_move
def play_game():
    board = [[EMPTY] * 3 for _ in range(3)]

    current_player = PLAYER_X

    while True:
        print_board(board)

        if current_player == PLAYER_X:
   
            print("Your turn (Player X):")
            row = int(input("Enter row (0, 1, 2): "))
            col = int(input("Enter column (0, 1, 2): "))
            
            if board[row][col] != EMPTY:
                print("Cell is already taken. Try again.")
                continue
            
            board[row][col] = PLAYER_X
            if check_winner(board, PLAYER_X):
                print_board(board)
                print("Player X wins!")
                break
            current_player = PLAYER_O 
        else:
            print("AI's turn (Player O):")
            row, col = find_best_move(board)
            board[row][col] = PLAYER_O
            if check_winner(board, PLAYER_O):
                print_board(board)
                print("AI wins!")
                break
            current_player = PLAYER_X

        if check_draw(board):
            print_board(board)
            print("It's a draw!")
            break

if __name__ == "__main__":
    play_game()
