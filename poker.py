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


def isRoyalFlush(hand):
    suits=[]
    values=[]
    hand=hand.split(" ")
    # return hand
    for i in range(len(hand)):
        values.append(hand[i][0])
        suits.append(hand[i][1])

    if suits[0]==suits[1] and suits[1]==suits[2] and suits[2]==suits[3] and suits[3]==suits[4]:
        # print("suitssame")
        list=["T","Q","A","J","K"]
        for i in list:
            # print(i)
            if i not in values:
                return 0
        return 10
    return 0

# print(isRoyalFlush("TH JH QH KH AH"))

def StraightFlush(hand):
    values=[]
    suits=[]
    hand=hand.split(" ")

    card_values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}

    for card in hand:
        values.append(int(card_values[card[0]]))
        suits.append(card[1])
    values=sorted(values)

    for i in range(len(values)-1):
        if values==[1,2,3,4,14] and suits[0]==suits[1] and suits[1]==suits[2] and suits[2]==suits[3] and suits[3]==suits[4]:
            return 9
        if int(values[i])-int(values[i+1])!=-1:
            return 0
        elif suits[0]==suits[1] and suits[1]==suits[2] and suits[2]==suits[3] and suits[3]==suits[4]:
            return 9
# print(StraightFlush("AH JH 4H KH TH"))


def FourOfKind(hand):
    values=[]
    suits=[]
    hand=hand.split(" ")

    dic={}

    for card in hand:
        values.append(int(card_values[card[0]]))
        suits.append(card[1])
    for i in values:
        if i in dic:
            dic[i]+=1
        else:
            dic[i]=1

    for v in dic.values():
        if v==4:
            return True
    return False
# print(FourOfKind("2H AH AH AH TH"))
# print(FourOfKind("2H 2H 3H 2S 4G"))


def FullHouse(hand):
    values=[]
    suits=[]
    hand=hand.split(" ")

    dic={}

    for card in hand:
        values.append(int(card_values[card[0]]))
        suits.append(card[1])
    for i in values:
        if i in dic:
            dic[i]+=1
        else:
            dic[i]=1
    house=[]
    for each in dic:
        if dic[each]==3 or dic[each]==2:
            house.append(dic[each])
    if 3 in house and 2 in house:
        return True
    return False
# print(FullHouse("AH AD AS 5S 5D"))

def Flush(hand):
    suits=[]
    hand=hand.split(" ")

    for card in hand:
        suits.append(card[1])
    if suits[0]==suits[1] and suits[1]==suits[2] and suits[2]==suits[3] and suits[3]==suits[4]:
        return True
    return False

# print(Flush("AH 6S AS 5S 5S"))


def Straight(hand):
    values=[]
    hand=hand.split(" ")

    for card in hand:
        values.append(int(card_values[card[0]]))
    values.sort()

    for i in range(len(values)-1):
        if values==[1,2,3,4,14]:
            return True
        if int(values[i])-int(values[i+1])!=-1:
            return False
        return True
    
# print(Straight("AH 2S 3S 4S 5S"))

def ThreeOfKind(hand):
    values=[]
    hand=hand.split(" ")

    dic={}

    for card in hand:
        values.append((card_values[card[0]]))
    
  
    for i in values:
        if i in dic:
            dic[i]+=1
        else:
            dic[i]=1

    for v in dic.values():
        if v==3 or v==4 or v==5:
            return True
    return False

# print(ThreeOfKind("AD AS AS 4S 5S"))
# print(ThreeOfKind("KH KD KS KS KS"))


def TwoPairs(hand):
    values=[]
    hand=hand.split(" ")
    for card in hand:
        values.append(card_values[card[0]])
    
    dic={}
    for i in values:
        if i in dic:
            dic[i]+=1
        else:
            dic[i]=1
    pairs=0
    for i in dic.values():
        if i==2:
            pairs+=1
        
    if pairs==2:
        return True

    return False

# print(TwoPairs("5D AS 3S 3S 5S"))
# print(TwoPairs("5D AS 3S 3S 5S"))


def OnePair(hand):
    values=[]
    hand=hand.split(" ")
    for card in hand:
        values.append(card_values[card[0]])
    
    dic={}
    for i in values:
        if i in dic:
            dic[i]+=1
        else:
            dic[i]=1
   
    for i in dic.values():
        if i==2:
            return True
        

    return False
# print(OnePair("6D AS 3S 3S 5S"))

def highestCard(hand):
    hand=hand.split()
    values=[]
    for i in hand:
        values.append(card_values[i[0]])

    return max(values)
# print(highestCard("6D 7S KS 3S 5S"))


def findRank(hand):
    if isRoyalFlush(hand):
        return 10
    elif StraightFlush(hand):
        return 9
    elif FourOfKind(hand):
        return 8
    elif FullHouse(hand):
        return 7
    elif Flush(hand):
        return 6
    elif Straight(hand):
        return 5
    elif ThreeOfKind(hand):
        return 4
    elif TwoPairs(hand):
        return 3
    elif OnePair(hand):
        return 2
    else:
        return 1

def poker(hands):
    # print("fhvbf vi: ",hands)
    rank1=findRank(hands[0])
    rank2=findRank(hands[1])