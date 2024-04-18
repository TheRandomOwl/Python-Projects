# tic-tac-toe game

grid = [[' ',' ',' '],
        [' ',' ',' '],
        [' ',' ',' ']
        ]
def enter_move(player, symbol):
    show_grid()
    while True:
        try:
            row = int(input(f"{player} enter a row: "))
            column = int(input(f"{player} enter a column: "))
            if grid[row][column] == ' ':
                grid[row][column] = symbol
                break
            else:
                print("This location is already taken.")
        except IndexError:
            print("Invalid range")
        except ValueError:
            print("Please enter a number")

def show_grid(): # 3 x 3 grid
    print(f"╔═══╦═══╦═══╗\n║ {grid[0][0]} ║ {grid[0][1]} ║ {grid[0][2]} ║\n╠═══╬═══╬═══╣\n║ {grid[1][0]} ║ {grid[1][1]} ║ {grid[1][2]} ║\n╠═══╬═══╬═══╣\n║ {grid[2][0]} ║ {grid[2][1]} ║ {grid[2][2]} ║\n╚═══╩═══╩═══╝")

def check_win():
    game_over = False
    # Check rows
    for row in grid:
        if ('OOO' in ''.join(row) or 'XXX' in ''.join(row)):
            game_over = True

    # Check columns
    for col in range(3):
        if (grid[0][col] == grid[1][col] == grid[2][col] and grid[0][col] != ' '):
            game_over = True

    # Check diagonals
    if (grid[0][0] == grid[1][1] == grid[2][2] or grid[0][2] == grid[1][1] == grid[2][0]) and (grid[1][1] != ' '):
        game_over = True
        
    show_grid()
    return game_over

for i in range(5):
    enter_move('Player 1','X')
    if check_win():
        print("Player 1 wins!")
        break
    if (i < 4): enter_move('Player 2','O') # prevent player 2 from getting stuck in loop
    if check_win():
        print("Player 2 wins!")
        break
    print(''.join(grid[0]))
else:
    print("Tie")
