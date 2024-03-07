# program : connect four game
#author : maryam ayman mosad youssef  20230390
#version :1.85.1
#date : 1/3/2024

def win(player, board):

    # probabilities for player to win
    for row in board:
        for x in range(4):
            if all(piece == player for piece in row[x:x+4]):
                return True
            
    
    for col in range(7) :
        for x in range(3):
            if all(row[col]== player for row in board[x:x+4]):
                return True
    
    for row in range(3):
        for col in range (4):
            if all(board[row+x][col+x]== player for x in range(4)):
                return True

    for row in range(3, 6):
        for col in range(4):
            if all(board[row-x][col+x]== player for x in range(4)):
                return True
            
    return False 
            
def full_board(board):
    return all(piece!= " " for row in board for piece in row)

def main():
    board = [[' '  for _ in range (7)] for _ in range(6)]

    player = "X"

    while True:
        print(board)
        coloumn = int(input(f"player{player} enter a col 0-6:"))

        if coloumn < 0 or coloumn > 6:
            print("please enter a valid choise")

        for row in range (5, -1, -1):
            if board[row][coloumn] == " ":
                board[row][coloumn] = player
                break
            else:
                print("the coloumn you choose is full!")
                continue

        if win(player, board):
            print(board)
            print(f"player{player} wins!")
            break

        if full_board(board):
            print(board)
            print('draw!')
            break

        player = "O" if player =="X" else "X"

main()



x in range(4)):
                return True
            
    return False 
            
def full_board(board):
    return all(piece!= " " for row in board for piece in row)

def main():
    board = [[' '  for _ in range (7)] for _ in range(6)]

 