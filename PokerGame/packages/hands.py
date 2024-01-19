def determine_hand(hand):
    card_value = dict(zip('2 3 4 5 6 7 8 9 T J Q K A'.split(), range(14)))

    cards = []
    suits = []

    for card in hand.split():
        c, s = list(card)
        cards.append(c)
        suits.append(s)

    max_suit = max([suits.count(a) for a in suits])
    same_cards = sorted([cards.count(a) for a in set(cards)])
    card_nums = sorted([card_value[a] for a in cards])

    def is_straight(cv):
        diff = cv[-1] - cv[0]
        if diff == 4:
            return True
        elif diff == 12:
            if cv[-2] - cv[0] == 3:
                return True
        return False

    # We have our flushes in here. Any less suits and we don't care.
    if max_suit == 5:
        if is_straight(card_nums):
            if card_nums[0] == 8: # ROYAL FLUSH!!!
                return "Royal Flush"
            return "Straight Flush"
        return "Flush"

    # Checking in on our same cards
    # With a length of two we either have two pair or a full house
    elif len(same_cards) == 2:
        if max(same_cards) == 4: # Four of a Kind
            return "Four of a Kind"
        elif max(same_cards) == 3: # Full House
            return "Full House"
    elif len(same_cards) == 3:
        if max(same_cards) == 3: # Three of a kind
            return "Three of a Kind"
        else: # Two pair
            return "Two Pair"
    elif len(same_cards) == 4:
        return "One Pair"
    else: # Garbage hand most likely. But maybe a straight!
        if is_straight(card_nums):
            return "Straight"
        return "High Card"

if __name__ == "__main__":
    hands = ["TS JS QS KS AS", # Royal Flush
             "AC 2C 3C 4C 5C", # Straight Flush
             "AC AS 3C AD AH", # Four of a Kind
             "TC 2C 2H TS TH", # Full House
             "AH 5H TH 7H 4H", # Flush
             "3D 4C 5H 6C 7D", # Straight
             "3D 3C 3S 5H AD", # Three of a Kind
             "3D 3C 5H 5S 7D", # Two Pair
             "3D 3C 5H 8S 7D", # One Pair
             "AC 3C 4H 7S 2D"] # High Card Garbage

    for hand in hands:
        print ("With a hand of {}, Bob has a {}!".format(hand, determine_hand(hand)))