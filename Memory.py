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

def pickedCard(dic, card1, card2):
    """Checks if two picked cards are a matching pair."""
    if dic[card1] == dic[card2]:
        print(dic[card1], dic[card2])
        print("You picked the same pair. Continue to pick the remaining cards.")
        return True
    else:
        print(dic[card1], dic[card2])
        print("You picked unpaired cards. Please try again.")
        return False
    

def play():
    """Main function to play the memory game."""
    print("Welcome to the memory game")
    board = generateBoard()
    dic = {
        "00": board[0], "01": board[1], "02": board[2], "03": board[3],
        "10": board[4], "11": board[5], "12": board[6], "13": board[7],
        "20": board[8], "21": board[9], "22": board[10], "23": board[11],
        "30": board[12], "31": board[13], "32": board[14], "33": board[15]
    }
    
    print(dic)
    print('''The board is a 4x4 matrix, each card position is a combination of row and column.
              For example, the first element's position is 00 which is row=0:col=0,
              and the second element's position is 01 which is row=0:col=1.''')

    revealed_pairs = 0
    while revealed_pairs < 8:
        print("You need to reveal all pairs to win the game.")
        print("Enter 'exit' to end the game.")
        display_board(board)
        
        choice1 = input("Enter your card1 position to open: ")
        if choice1.lower() == "exit":
            break
        choice2 = input("Enter your card2 position to open: ")
        if choice2.lower() == "exit":
            break
      
        if pickedCard(dic, choice1, choice2):
            revealed_pairs += 1
            card = dic[choice1]
            markNumber(board, card)
            display_board(board)
            print(f"Pairs revealed: {revealed_pairs}")
            
    print("You correctly picked all the pairs! Congratulations!")

play()