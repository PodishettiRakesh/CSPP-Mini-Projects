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

# Step 5: Slide and merge a row to the left
def slide_and_merge_row_left(row):
    new_row = [0, 0, 0, 0]
    insert_pos = 0
    last_value = 0
    for i in range(4):
        if row[i] != 0:
            if last_value == 0:
                last_value = row[i]
            elif last_value == row[i]:
                new_row[insert_pos] = 2 * row[i]
                insert_pos += 1
                last_value = 0
            else:
                new_row[insert_pos] = last_value
                insert_pos += 1
                last_value = row[i]
    if last_value != 0:
        new_row[insert_pos] = last_value
    return new_row
# row = [2, 2, 4, 4]
# new_row = slide_and_merge_row_left(row)
# print(new_row)  # Output: [4, 8, 0, 0]


# Step 8: Move up
def move_up(grid):
    for j in range(4):
        col = [grid[i][j] for i in range(4)]
        new_col = slide_and_merge_row_left(col)
        for i in range(4):
            grid[i][j] = new_col[i]

# Step 9: Move down
def move_down(grid):
    for j in range(4):
        col = [grid[i][j] for i in range(4)]
        new_col = list(reversed(slide_and_merge_row_left(list(reversed(col)))))
        for i in range(4):
            grid[i][j] = new_col[i]
