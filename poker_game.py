# In the card game poker, a hand consists of five cards and are ranked, from lowest to highest, in the 
# following way:
# High Card: Highest value card.
# One Pair: Two cards of the same value.
# Two Pairs: Two different pairs.
# Three of a Kind: Three cards of the same value.
# Straight: All cards are consecutive values.
# Flush: All cards of the same suit.
# Full House: Three of a kind and a pair.
# Four of a Kind: Four cards of the same value.
# Straight Flush: All cards are consecutive values of the same suit.
# Royal Flush: Ten, Jack, Queen, King, Ace, in the same suit.
# More on Poker Hands (https:#en.wikipedia.org/wiki/List_of_poker_hands)
# The cards are valued in the order:
# 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace

# If two players have the same ranked hands then the rank made up of the highest value wins; for 
# example, a pair of eights beats a pair of fives. But if two ranks tie, for 
# example, both players have a pair of queens, then highest cards in each hand are compared; if the highest 
# cards tie then the next highest cards are compared, and so on. 

card_values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
