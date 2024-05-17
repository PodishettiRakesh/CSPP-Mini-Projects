import random

def generateBoard():
    """Generates and returns a shuffled board with pairs of cards."""
    cards = ["A", "C", "B", "D", "E", "F", "G", "H"]
    totalcards = cards * 2
    random.shuffle(totalcards)
    return totalcards


guessed = []
def display_board(board):
    """Displays the current state of the board, showing guessed cards and hiding unguessed ones."""
    for i in range(0, len(board), 4):
        row = board[i:i+4]
        for card in row:
            if card in guessed:
                print(card, end="  ")
            else:
                print("*", end="  ")
        print("\n")

def markNumber(board, card):
    """Marks a card as guessed if it has been picked."""
    for i in range(0, len(board), 4):
        row = board[i:i+4]
        for i in row:
            if card == i:
               guessed.append(i)
    return board