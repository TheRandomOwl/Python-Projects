# Connect Four

# create an array to store the board   
board = [[] for x in range(7)]

def print_board():
    for y in range(5, -1, -1):
        print("|", end="")
        for x in range(7):
            if len(board[x]) > y:
                print(board[x][y], end="")
            else:
                print(" ", end="")
            print("|", end="")
        print()
    print("---------------")
    print(" 1 2 3 4 5 6 7")

def player_move(player):
    while True:
        try:
            col = int(input("Player " + player + ", enter a column (1-7): ")) - 1
            if col < 0 or col > 6:
                print("Column out of range.")
            elif len(board[col]) == 6:
                print("Column is full.")
            else:
                board[col].append(player)
                break
        except ValueError:
            print("Invalid input.")

def check_win():
    for y in range(7):
        if 'XXXX' in "".join(board[y]) or 'OOOO' in "".join(board[y]):
            return True
    for x in range(7):
        pass
print_board()
print(board)
while True:
    player_move("X")
    print_board()
    if check_win():
        print("Player X wins!")
        break
    player_move("O")
    print_board()
    if check_win():
        print("Player O wins!")
        break
    if all(len(col) == 6 for col in board):
        print("It's a tie!")
        break