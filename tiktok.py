import tkinter as tk
import math

# Constants for players
PLAYER_X, PLAYER_O, EMPTY = 1, -1, 0

# Minimax Algorithm
def minimax(board, is_max):
    winner = check_winner(board)
    if winner: return winner
    if all(cell != EMPTY for cell in board): return 0
    best = -math.inf if is_max else math.inf
    for i in range(9):
        if board[i] == EMPTY:
            board[i] = PLAYER_X if is_max else PLAYER_O
            best = max(best, minimax(board, False)) if is_max else min(best, minimax(board, True))
            board[i] = EMPTY
    return best

def check_winner(board):
    for i in range(3):
        if abs(board[i*3] + board[i*3+1] + board[i*3+2]) == 3: return board[i*3]
        if abs(board[i] + board[i+3] + board[i+6]) == 3: return board[i]
    if abs(board[0] + board[4] + board[8]) == 3: return board[0]
    if abs(board[2] + board[4] + board[6]) == 3: return board[2]
    return 0

def best_move(board):
    best, move = -math.inf, -1
    for i in range(9):
        if board[i] == EMPTY:
            board[i] = PLAYER_X
            score = minimax(board, False)
            if score > best:
                best, move = score, i
            board[i] = EMPTY
    return move

def reset_game():
    global board
    board = [EMPTY] * 9
    for btn in buttons:
        btn.config(text="", state=tk.NORMAL, bg="lightblue")

def button_click(index):
    if board[index] == EMPTY:
        board[index] = PLAYER_X
        buttons[index].config(text="X", state=tk.DISABLED, bg="lightgreen")
        winner = check_winner(board)
        if winner: show_result(f"Player X wins!")
        elif all(cell != EMPTY for cell in board): show_result("It's a draw!")
        else:
            computer_move()

def computer_move():
    move = best_move(board)
    board[move] = PLAYER_O
    buttons[move].config(text="O", state=tk.DISABLED, bg="lightcoral")
    winner = check_winner(board)
    if winner: show_result(f"Computer O wins!")
    elif all(cell != EMPTY for cell in board): show_result("It's a draw!")

def show_result(message):
    for btn in buttons:
        btn.config(state=tk.DISABLED)
    tk.messagebox.showinfo("Game Over", message)
    reset_game()

# Tkinter Setup
root = tk.Tk()
root.title("Tic Tac Toe")
buttons = []
board = [EMPTY] * 9

for i in range(9):
    btn = tk.Button(root, text="", font=("Arial", 24), width=5, height=2, bg="lightblue", command=lambda i=i: button_click(i))
    btn.grid(row=i // 3, column=i % 3, padx=5, pady=5)
    buttons.append(btn)

reset_btn = tk.Button(root, text="Reset", font=("Arial", 16), bg="orange", fg="white", command=reset_game)
reset_btn.grid(row=3, column=0, columnspan=3, sticky="nsew", padx=5, pady=5)

root.mainloop()
