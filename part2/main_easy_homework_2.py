import os
import random 


print("Game tic-tac-toe\n")

# Імплементація ігрового поля
select_size = input("Select size of board NxN (default = 3): ")
N = int(select_size) if select_size else 3

board = [[" " for _ in range(N)] for _ in range(N)]

            # board = []
            # for i in range(3):
            #     row = []
            #     for j in range(3):
            #         row.append(' ')
            #     board.append(row)

ai = input("do you want to play against AI? 'y': ")
print(f"play with ai = {ai}")


current_player = "X"
count_games = 1


while True:
    print("Game tic-tac-toe\n")  
    
    
    # show board
    for i in range(1,len(board)+1):
        print(f"    {i}", end = '')
    print()
    for i, row in enumerate(board, 1):
        print(i, row)
    
    
    
    # 2) player`s move
    print(f"Move player {current_player}")
    
    # if AI move AI
    if current_player == 'O' and ai:
        # Проверка строк и столбцов на возможность блокировки
        for i in range(3):
            # Проверка строк
            if board[i].count('X') == 2 and board[i].count(' ') == 1:
                col = board[i].index(' ')
                board[i][col] = 'O'
                
            
            # Проверка столбцов
            col_vals = [board[r][i] for r in range(3)]
            if col_vals.count('X') == 2 and col_vals.count(' ') == 1:
                row = col_vals.index(' ')
                board[row][i] = 'O'
                current_player == "X"
                continue

        # Проверка диагоналей на возможность блокировки
        diag1 = [board[i][i] for i in range(3)]
        if diag1.count('X') == 2 and diag1.count(' ') == 1:
            empty_index = diag1.index(' ')
            board[empty_index][empty_index] = 'O'
            current_player == "X"
            continue

        diag2 = [board[i][2 - i] for i in range(3)]
        if diag2.count('X') == 2 and diag2.count(' ') == 1:
            empty_index = diag2.index(' ')
            board[empty_index][2 - empty_index] = 'O'
            current_player == "X"
            continue
        
        # Если нет возможности заблокировать, то выбираем случайную клетку
        empty_cells = [(r, c) for r in range(3) for c in range(3) if board[r][c] == " "]
        move = random.choice(empty_cells)
        board[move[0]][move[1]] = 'O'

    # ==========================================================
    
    else:
        while True:
            coords = input("Enter coordinates as 'row col': ")
            try:
                coords = coords.split()
                row, col = int(coords[0]), int(coords[1])    
            except: 
                print("Enter coordinates as two numbers 'row col'")
                continue        
            
            # check if index is out of the range   
            if row not in range(1, len(board)+1) and col not in range(1, len(board)+1):
                print(f"Incorrect value {row} or {col}")
                continue
            
            # check if cell is not empty   
            if board[row-1][col-1] != " ":
                print(f"field {row} {col} is busy")
                continue
            
            board[row-1][col-1] = current_player
            break
    
    # 3) Check Draw
    if all([cell != " " for row in board for cell in row]):        
        print("Draw!")
        break

                                                    # for row in board:
                                                    #     for cell in row:
                                                    #         if cell == " ":
                                                    #             continue
                                                    #         else:
                                                    #             print("Draw!")
                                                    #             break
                        
                        
    # 4) Перевірка умов виграшу
    winner = None
    for row in range(len(board)):        
        if all(board[row][col] == current_player for col in range(len(board))): 
            winner = True
        elif all(board[col][row] == current_player for col in range(len(board))):
            winner = True
    
    if all(board[i][i] == current_player for i in range(len(board))) or all(board[i][len(board)-1-i] == current_player for i in range(len(board))):
        winner = True                    
                        
    # Check winner
    if winner:
        
        # show board
        for i in range(len(board)):
            print(f"    {i}", end = '')
            print()
        for i, row in enumerate(board, 0):
            print(i, row)
            
        print("Draw!") if winner == 2 else print(f"win player {current_player}")
        reset = input("press 'Y' for paly again: ")
        if reset == "y":
            board = [[" " for _ in range(N)] for _ in range(N)]
            count_games+=1
            continue
        break
        
    # 5) Зміна гравця
    current_player = "O" if current_player == "X" else "X"
    # os.system("clear")


print(f"Your played {count_games} games!")
print("End Game")
