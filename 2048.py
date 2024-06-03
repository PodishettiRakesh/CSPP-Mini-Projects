import random

# Step 1: Initialize the grid
def initialize_grid():
    grid = [[0 for _ in range(4)] for _ in range(4)]
    add_new_tile(grid)
    add_new_tile(grid)
    return grid


# Step 2: Add a new tile
def add_new_tile(grid):
    empty_positions = []
    for i in range(4):
        for j in range(4):
            if grid[i][j] == 0:
                empty_positions.append((i, j))
    if empty_positions:
        x, y = random.choice(empty_positions)
        grid[x][y] = 2 if random.random() < 0.9 else 4


# Step 3: Print the grid
def print_grid(grid):
    for row in grid:
        print(" ".join([str(cell).ljust(5) for cell in row]))
    print()
# grid=initialize_grid()
# print_grid(grid)


# Step 4: Get user input
def get_user_input():
    move = input("Enter move (W/A/S/D): ").upper()
    while move not in ('W', 'A', 'S', 'D'):
        move = input("Invalid input. Enter move (W/A/S/D): ").upper()
    return move
# print(get_user_input())