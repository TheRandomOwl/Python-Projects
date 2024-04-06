# tic-tac-toe game
player1 = {
    "name": 'Player 1',
    "row": 0,
    "column": 0,
    "symbol": 'X'
}
player2 = {
    "name": 'Player 2',
    "row": 0,
    "column": 0,
    "symbol": 'O'
}

grid = [[' ',' ',' '],
        [' ',' ',' '],
        [' ',' ',' ']
        ]
def enter_move(player):
    player["row"] = int(input(f"{player['name']} enter a row: "))
    player["column"] = int(input(f"{player['name']} enter a column: "))
    grid[player["row"]][player["column"]] = player["symbol"]

def show_grid(): # 3 x 3 grid
    print(f"╔═══╦═══╦═══╗\n║ {grid[0][0]} ║ {grid[0][1]} ║ {grid[0][2]} ║\n╠═══╬═══╬═══╣\n║ {grid[1][0]} ║ {grid[1][1]} ║ {grid[1][2]} ║\n╠═══╬═══╬═══╣\n║ {grid[2][0]} ║ {grid[2][1]} ║ {grid[2][2]} ║\n╚═══╩═══╩═══╝")

show_grid()
for i in range(9):
    enter_move(player1)
    enter_move(player2)
    show_grid()
