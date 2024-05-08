import random
cards=["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
deckOfCards=cards*4
# print(deckOfCards)]
cardValues={"A":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"J":10,"Q":10,"K":10}

def dealCards(cards):
    random.shuffle(cards)
    # print(cards)
    player1_cards=cards[-1:-6:-1]
    for each in player1_cards:
        deckOfCards.remove(each)
    return player1_cards
# print(dealCards(deckOfCards))

def cardValue(card):
    return cardValues[card]
# print(cardValue("2"))


def main():
    print("welcome to the pycards game")
    player1=dealCards(deckOfCards)
    # print(player1)
    player2=dealCards(deckOfCards)
    # print(player1)
    # print(player2)
    player1Score=0
    player2Score=0
    totalCards=len(player1)

    while totalCards!=0 :
        p1=int(input("enter the card to be drawn for player1: "))
        if p1<=len(player1):
        
            card1=player1[p1-1]
        else:
            print("please enter valid card number")
            continue

        # print(card1)
        # print(player1)
        p2=int(input("enter the card to be drawn for player2: "))
        if p2<=len(player2):
            card2=player2[p2-1]
        else:
            print("please enter valid card number")
            continue
        player1.pop(p1-1)
        player2.pop(p2-1)

        # print(card2)

        if cardValue(card1)==cardValue(card2):
            print("both card values are same, this round is Tie")
        elif cardValue(card1)>cardValue(card2):
            print(f"player1 card value is high, this round winner is player 1")
            player1Score+=cardValue(card1)+cardValue(card2)
            print(f"the updated score are player1 score {player1Score} and player 2 score: {player2Score}")
        elif cardValue(card1)<cardValue(card2):
            print("player2 card value is high, this round winner is player 2")
            player2Score+=cardValue(card1)+cardValue(card2)
            print(f"the updated score are player1 score: {player1Score} and player 2 score: {player2Score}")
        totalCards+=-1
        print("\n")
    
    if player1Score>player2Score:
        print("game winner is player1! :)")
    elif player1Score<player2Score:
        print("game winner is player2 :)")
    else:
        print("both player scores are equal , this game end as Tie")




        
main()