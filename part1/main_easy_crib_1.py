import os

print("Game tic-tac-toe\n")

# Імплементація ігрового поля
board = [ 
         [" ", " ", " "], 
         [" ", " ", " "], 
         [" ", " ", " "]
]

current_player = "X"

while True:
    print("Game tic-tac-toe\n")  
    
    
    # show board
    print("    1    2    3")
    for i, row in enumerate(board, 0):
        print(i, row)
    
    # 2) player`s move
    print(f"Move player {current_player}")
    
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
            print(f"incorrect value {row} or {col}")
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
        print(f"Player {current_player} win!")
        break
        
    # 5) Зміна гравця
    current_player = "O" if current_player == "X" else "X"
    os.system("clear")


# show board
print("    1    2    3")
for i, row in enumerate(board, 1):
    print(i, end="")
    print(row)

print("End Game")
