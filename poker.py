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


def is_Royal_Flush(hand):
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

# print(is_Royal_Flush("TH JH QH KH AH"))

def Straight_Flush(hand):
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
# print(Straight_Flush("AH JH 4H KH TH"))


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


def Full_House(hand):
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
# print(Full_House("AH AD AS 5S 5D"))

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


def Two_Pairs(hand):
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

# print(Two_Pairs("5D AS 3S 3S 5S"))
# print(Two_Pairs("5D AS 3S 3S 5S"))


def One_Pair(hand):
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
# print(One_Pair("6D AS 3S 3S 5S"))

def Highest_cardValue(hand):
    hand=hand.split()
    values=[]
    for i in hand:
        values.append(card_values[i[0]])

    return max(values)
# print(Highest_cardValue("6D 7S KS 3S 5S"))

# ------------------------------------------------------------------------------
def findRank(hand):
    if is_Royal_Flush(hand):
        return 10
    elif Straight_Flush(hand):
        return 9
    elif FourOfKind(hand):
        return 8
    elif Full_House(hand):
        return 7
    elif Flush(hand):
        return 6
    elif Straight(hand):
        return 5
    elif ThreeOfKind(hand):
        return 4
    elif Two_Pairs(hand):
        return 3
    elif One_Pair(hand):
        return 2
    else:
        return 1
def Staright_Flush_Tie(hands):
    r1=Highest_cardValue(hands[0])
    r2=Highest_cardValue(hands[1])
    if r1>r2:
        return hands[0]
    elif r2>r1:
        return hands[1]
def FourOfKind_Tie(hands):
    d1 = {}
    d2 = {}
    
    hand = hands[0].split(" ")
    for i in hand:
        if i[0] in d1:
            d1[i[0]] += 1
        else:
            d1[i[0]] = 1
        
    hand = hands[1].split(" ")
    for i in hand:
        if i[0] in d2:
            d2[i[0]] += 1
        else:
            d2[i[0]] = 1

    f1 = 0
    f2 = 0
    for k,v in d1.items():
        if d1[k] == 4:
            f1 = k
        else:
            f2 = k
    f3 = 0
    f4 = 0       
    for k,v in d2.items():
        if d2[k] == 4:
            f3 = k
        else:
            f4 = k 
    if f1 > f3:
        return hands[0]
    elif f3 > f1:
        return hands[1]
    else:
        if f2 > f4:
            return hands[0]
        elif f4 > f2:
            return hands[1]
        
def Full_House_Tie(hands):
    d1 = {}
    d2 = {}
    
    hand = hands[0].split(" ")
    for i in hand:
        if i[0] in d1:
            d1[i[0]] += 1
        else:
            d1[i[0]] = 1

    hand = hands[1].split(" ")
    for i in hand:
        if i[0] in d2:
            d2[i[0]] += 1
        else:
            d2[i[0]] = 1
    f1 = 0
    f2 = 0
    for k,v in d1.items():
        if d1[k] == 3:
            f1 = k
        elif d1[k] == 2:
            f2 = k
    f3 = 0
    f4 = 0       
    for k,v in d2.items():
        if d2[k] == 3:
            f3 = k
        elif d2[k] == 2:
            f4 = k 
    
    if f1 > f3:
        return hands[0]
    elif f3 > f1:
        return hands[1]
    else:
        if f2 > f4:
            return hands[0]
        elif f4 > f2:
            return hands[1]
        
def Flush_Tie(hands):
    hand = hands[0].split(" ")
    values1 = []
    for i in hand:
        if i[0] == 'T' or i[0] == 'K' or i[0] =='J' or i[0] == 'Q' or i[0] == 'A':
            values1.append(card_values[i[0]])
        else:
            values1.append(int(i[0]))   
    values1 = sorted(values1)

    hand = hands[1].split(" ")
    values2 = []
    for i in hand:
        if i[0] == 'T' or i[0] == 'K' or i[0] =='J' or i[0] == 'Q' or i[0] == 'A':
            values2.append(card_values[i[0]])
        else:
            values2.append(int(i[0]))   
    values2 = sorted(values2)

    for i in range(4, -1, -1):
        if values1[i] > values2[i]:
            return hands[0]
        elif values2[i] > values1[i]:
            return hands[1]


def ThreeOfKind_Tie(hands):
    d1 = {}
    d2 = {}
    
    hand = hands[0].split(" ")
    for i in hand:
        if i[0] in d1:
            d1[i[0]] += 1
        else:
            d1[i[0]] = 1

    hand = hands[1].split(" ")
    for i in hand:
        if i[0] in d2:
            d2[i[0]] += 1
        else:
            d2[i[0]] = 1
    f1 = 0
    l1 = []
    for k,v in d1.items():
        if d1[k] == 3:
            f1 = k
        else:
            l1.append(k)

    f2 = 0
    l2 = []
    for k,v in d2.items():
        if d2[k] == 3:
            f2 = k
        else:
            l2.append(k)

    if f1 > f2:
        return hands[0]
    elif f2 > f1:
        return hands[1]
    else:
        l1 = sorted(l1)
        l2 = sorted(l2)
        if l2[1] > l1[1]:
            return hands[1]
        elif l1[1]>l2[1]:
            return hands[0]
        else:
            if l1[0] > l2[0]:
                return hands[0]
            elif l2[0] > l1[0]:
                return hands[1]




def Two_Pairs_Tie(hands):
    d1 = {}
    d2 = {}
    
    hand = hands[0].split(" ")
    for i in hand:
        if i[0] in d1:
            d1[i[0]] += 1
        else:
            d1[i[0]] = 1

    hand = hands[1].split(" ")
    for i in hand:
        if i[0] in d2:
            d2[i[0]] += 1
        else:
            d2[i[0]] = 1
    
    l1 = []
    v1 = 0
    for k,v in d1.items():
        if d1[k] == 2:
            l1.append(k)
        else:
            v1 = k
    l2 = []
    v2 = 0
    for k,v in d2.items():
        if d2[k] == 2:
            l2.append(k)
        else:
            v2 = k

    l1 = sorted(l1)    
    l2 = sorted(l2)    

    if l1[1] > l2[1]:
        return hands[0]
    elif l2[1] > l1[1]:
        return hands[1]
    else:
        if l1[0] > l2[0]:
            return hands[0]
        elif l2[0] > l1[0]:
            return hands[1]
        else:
            if v1 > v2:
                return hands[0]
            elif v2 > v1:
                return hands[1]
# --------------------------------------------------------------
def tiebreak(hands,rank):
    if rank==9:
        return Staright_Flush_Tie(hands)
    elif rank==8:
        return FourOfKind_Tie(hands)
    elif rank==7:
        return Full_House_Tie(hands)
    elif rank == 6:
        return Flush_Tie(hands)
    elif rank == 5:
        return Staright_Flush_Tie(hands)
    elif rank == 4:
        return ThreeOfKind_Tie(hands)
    elif rank == 3:
        return Two_Pairs_Tie(hands)
    elif rank == 1:
        return Flush_Tie(hands)

def poker(hands):
    rank1=findRank(hands[0])
    rank2=findRank(hands[1])

    if rank1 > rank2:
        return hands[0]
    elif rank2 > rank1:
        return hands[1]
    else:
        return tiebreak(hands, rank1)
    