import os
from  colorama import Fore, init
import random



def generate_board(N):
    # benerate board with size NxN
    return [[" " for _ in range(N)] for _ in range(N)]


def show_board():
    print(Fore.GREEN)
    for i in range(1, len(board)+1):        
        print(f"    {i}", end='')
    print("\n", "  ---" * len(board))
    for num, row in enumerate(board,1):    
        print(num, end=' ')
        for sign in row:
            color = Fore.BLUE if sign == "X" else Fore.RED                        
            print( "|", color+sign, Fore.GREEN+"|", end='')
        print("\n", "  ---" * len(board))

def player_move(board):   
    
    # Ход игрока
    print(Fore.RED + f"Move player {current_player}")
    
    while True:
        coords = input(Fore.YELLOW +"Enter coordinates 'row' 'col': ").split()
        try:
            row, col = map(int, coords)
        except:
            print("Enter coordinates as two numbers (row col)")
            continue
        
        if row not in range(1, len(board)+1) and col not in range(1, len(board)+1):
            print(f"uncorrect value {row} or {col}")
            continue
        
        if board[row-1][col-1] != " ":
            print(f"field {row} {col} is busy")
            continue
        
        board[row-1][col-1] = current_player
        return board
            
def check_win() -> bool:
     # Проверка победных условий: строки, столбцы и диагонали
    winner = False
    for row in range(len(board)):        
        if all(board[row][col] == current_player for col in range(len(board))): 
            winner = True
        elif all(board[col][row] == current_player for col in range(len(board))):
            winner = True
    
    if all(board[i][i] == current_player for i in range(len(board))) or all(board[i][len(board)-i-1] == current_player for i in range(len(board))):
        winner = True
    
    # Проверка на победу
    if winner:
        print(Fore.RED, f"Игрок {current_player} победил!")
        return winner 
    
    # Проверка на ничью
    if all(cell != " " for row in board for cell in row):        
        print(Fore.RED, "Ничья!")
        winner = True
    return winner  


def ai_move(board):
    print(Fore.RED + f"Move player AI as 'O'")
    empty_cells = [(r, c) for r in range(len(board)) for c in range(len(board[r])) if board[r][c] == " "]
    move = random.choice(empty_cells)
    board[move[0]][move[1]] = 'O'
    return board



def clever_ai_move(board):
    print(f"Move player AI as 'O'")
    
    # Проверка строк и столбцов на возможность блокировки
    for i in range(3):
        # Проверка строк
        if board[i].count('X') == 2 and board[i].count(' ') == 1:
            col = board[i].index(' ')
            board[i][col] = 'O'
            return board
        
        # Проверка столбцов
        col_vals = [board[r][i] for r in range(3)]
        if col_vals.count('X') == 2 and col_vals.count(' ') == 1:
            row = col_vals.index(' ')
            board[row][i] = 'O'
            return board

    # Проверка диагоналей на возможность блокировки
    diag1 = [board[i][i] for i in range(3)]
    if diag1.count('X') == 2 and diag1.count(' ') == 1:
        empty_index = diag1.index(' ')
        board[empty_index][empty_index] = 'O'
        return board

    diag2 = [board[i][2 - i] for i in range(3)]
    if diag2.count('X') == 2 and diag2.count(' ') == 1:
        empty_index = diag2.index(' ')
        board[empty_index][2 - empty_index] = 'O'
        return board
    
    # Если нет возможности заблокировать, то выбираем случайную клетку
    empty_cells = [(r, c) for r in range(3) for c in range(3) if board[r][c] == " "]
    move = random.choice(empty_cells)
    board[move[0]][move[1]] = 'O'
    return board
        
if __name__ == "__main__":   
    print("Game tic-tac-toe\n")
    
    count_games = 1
    current_player = "X"
    
    # Імплементація ігрового поля
    print(Fore.YELLOW)
    select_size = input("Select size of board (default = 3): ")
    N = int(select_size) if select_size else 3
    board = generate_board(N)  
    
    # Гра проти компьютера або проти гравця
    print(Fore.YELLOW)
    auto_game = input("Do you want to play against AI? 'Y': ")

    while 1:  
        # відобразити дошку
        show_board()   
        
        # хід гравця
        if current_player == 'O' and auto_game.lower() == "y":
            board = clever_ai_move(board)
        else:
            board = player_move(board)
            
        show_board()
        
        # перевірка на перемогу
        if check_win():
            print(Fore.YELLOW)
            replay = input("press 'Y' for play again: ")
            if replay.lower() == "y":
                count_games+=1
                board = generate_board(N)
                continue
            break
        
        current_player = "O" if current_player == "X" else "X"
        os.system("clear")
    
    print(Fore.BLUE)
    print(f"end game. Your played {count_games} games")
    