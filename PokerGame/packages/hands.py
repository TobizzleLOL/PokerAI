def determine_hand(hand):
    card_value = dict(zip('2 3 4 5 6 7 8 9 T J Q K A'.split(), range(14))) #Gives each card a value: 2 = 0, 3 = 1... A = 12

    cards = []
    suits = []
    aceTwoStraight = [0, 1, 2, 3, 12]

    for card in hand[0].split():
        c, s = list(card) # Splits the cards
        cards.append(c) #List all Kind of cards e.g ['A', '2', '3', '4', '5']
        suits.append(s) #List all Colors of the hand ['c', 'c', 'c', 'c', 'c']

    max_suit = max([suits.count(a) for a in suits]) #Counts the colors
    same_cards = sorted([cards.count(a) for a in set(cards)]) #Shows the duplicates e.g [2 (means pair), 1, 1, 1, 1]
    card_nums = sorted([card_value[a] for a in cards]) #Converted Cards to value e.g [0, 1, 2, 3, 12]

    def is_straight(cv):
        if(aceTwoStraight[0] in cv and
           aceTwoStraight[1] in cv and 
           aceTwoStraight[2] in cv and 
           aceTwoStraight[3] in cv and 
           aceTwoStraight[4] in cv):
            return True
        i = cv[0]
        j = 1
        while(i < 12):
            for j in range(4):
                i += 1
                if(i not in cv):
                    i = cv[1]
                    while(i < 12):
                        for j in range(4):
                            i += 1
                            if(i not in cv):
                                i = cv[2]
                                while(i < 12):
                                    for j in range(4):
                                        i += 1
                                        if(i not in cv):
                                            return False
                                    return True
                        return True
            return True


    # We have our flushes in here. Any less suits and we don't care.
    # 1 = High Card, 2: Pair, 3:Two Pair, 4: Three of a Kinds 5: Straight, 6: Flush, 7: Full-House, 8: Four of a Kind, 9: Straight-Flush, 10: Royal Flush
    if max_suit == 5:
        if is_straight(card_nums):
            if (card_nums[0] == 8 or card_nums[1] == 8 or card_nums[2] == 8): # ROYAL FLUSH!!!
                return 10
            return 9
        return 6

    # Checking in on our same cards
    # With a length of two we either have two pair or a full house
    elif len(same_cards) == 2:
        if max(same_cards) == 4: # Four of a Kind
            return 8
        elif max(same_cards) == 3: # Full House
            return 7
    elif len(same_cards) == 3:
        if max(same_cards) == 3: # Three of a kind
            return 4
        else: # Two pair
            return 3
    elif len(same_cards) == 4:
        return 2
    else: # Garbage hand most likely. But maybe a straight!
        if is_straight(card_nums):
            return 5
        return 1