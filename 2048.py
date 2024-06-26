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



# Step 4: Get user input
def get_user_input():
    move = input("Enter move (W/A/S/D): ").upper()
    while move not in ('W', 'A', 'S', 'D'):
        move = input("Invalid input. Enter move (W/A/S/D): ").upper()
    return move


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


# Step 6: Move up
def move_up(grid):
    for j in range(4):
        col = [grid[i][j] for i in range(4)]
        new_col = slide_and_merge_row_left(col)
        for i in range(4):
            grid[i][j] = new_col[i]

# Step 7: Move down
def move_down(grid):
    for j in range(4):
        col = [grid[i][j] for i in range(4)]
        new_col = list(reversed(slide_and_merge_row_left(list(reversed(col)))))
        for i in range(4):
            grid[i][j] = new_col[i]

# Step 8: Move left
def move_left(grid):
    for i in range(4):
        grid[i] = slide_and_merge_row_left(grid[i])

# Step 9: Move right
def move_right(grid):
    for i in range(4):
        grid[i] = list(reversed(slide_and_merge_row_left(list(reversed(grid[i])))))

# Step 10: Check win
def check_win(grid):
    for i in range(4):
        for j in range(4):
            if grid[i][j] == 2048:
                return True
    return False

# Step 11: Check game over
def check_game_over(grid):
    for i in range(4):
        for j in range(4):
            if grid[i][j] == 0:
                return False
            if i < 3 and grid[i][j] == grid[i+1][j]:
                return False
            if j < 3 and grid[i][j] == grid[i][j+1]:
                return False
    return True

# Step 12: Play game
def play_game():
    grid = initialize_grid()
    print_grid(grid)
    while True:
        move = get_user_input()
        if move == 'W':
            move_up(grid)
        elif move == 'A':
            move_left(grid)
        elif move == 'S':
            move_down(grid)
        elif move == 'D':
            move_right(grid)
        
        add_new_tile(grid)
        print_grid(grid)
        
        if check_win(grid):
            print("Congratulations! You reached 2048!")
            break
        if check_game_over(grid):
            print("Game over! No more valid moves.")
            break

if __name__ == "__main__":
    play_game()