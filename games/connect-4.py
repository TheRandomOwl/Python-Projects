# Connect Four

# create an array to store the board   
board = [[0] for x in range(7)]

def print_board():
    for y in range(6):
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
print_board()
print(board)
print(len(board[0]))