import random

def generateBoard():
    """Generates and returns a shuffled board with pairs of cards."""
    cards = ["A", "C", "B", "D", "E", "F", "G", "H"]
    totalcards = cards * 2
    random.shuffle(totalcards)
    return totalcards


guessed = []