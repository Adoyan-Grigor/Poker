"https://www.codewars.com/kata/5739174624fc28e188000465/train/python"

class PokerHand(object):

    RESULT = ["Loss", "Tie", "Win"]

    def __repr__(self):
        return self.hand

    def __init__(self, hand):
        self.hand = hand

    def straight_flush(self, hand):
        if self.hand_suit(hand) == 7 and self.sort_hand(hand) == 6:
            return 10
        return 0

    def kicker(self, hand, other):
        points = 0
        numbers = []
        my_res = 0
        other_res = 0
        gen = (i for i in "AKQJT98765432")
        card = next(gen)
        while True:
            for i in hand:
                if i[0] in card:
                    my_res += 1
            for i in other:
                if i[0] in card:
                    other_res += 1
            if my_res > other_res:
                return "Win"
            elif my_res < other_res:
                return "Loss"
            else:
                if card != "2":
                    card = next(gen)
                else:
                    return "Tie"
    
    def combinate(self, hand):
        points = 0
        hand.sort()
        exception = ""
        for i in range(len(hand)):
            combo = 0
            if i != len(hand) - 1:
                for l in hand[i+1:]:
                    if l[0] == hand[i][0] and hand[i][0] not in exception:
                        combo += 1
            exception += hand[i][0]
            if combo == 1:
                points += 2
            elif combo == 2:
                points += 5
            elif combo == 3:
                points += 9
        if points == 7:
            points = 8
        return points

    def sort_hand(self, hand):
        points = 0
        combo = []
        for i in hand:
            if i[0] == "A":
                combo.append(1)
                combo.append(14)
            elif i[0] == "T":
                combo.append(10)
            elif i[0] == "J":
                combo.append(11)
            elif i[0] == "Q":
                combo.append(12)
            elif i[0] == "K":
                combo.append(13)
            elif i[0] in "23456789":
                combo.append(int(i[0]))
        combo.sort()
        if 1 in combo and 2 not in combo:
            combo.remove(1)
        for i in range(len(combo)):
            if i != len(combo) - 1:
                if combo[i] + 1 != combo[i+1]:
                    break
            else:
                points += 6
        return points

    def hand_suit(self, hand):
        points = 0
        combo = []
        for i in hand:
            combo.append(i[-1])
        for i in range(len(combo)):
            if i != len(combo) - 1:
                if combo[i] != combo[i + 1]:
                    break
        else:
            points += 7
        return points
    
    def check_point(self):
        my_points = 0
        my_points += self.hand_suit(self.hand)
        if self.sort_hand(self.hand) > my_points:
            my_points = self.sort_hand(self.hand)
        if self.combinate(self.hand) > my_points:
            my_points = self.combinate(self.hand)
        return my_points

    def compare_with(self, other):
        self.hand = self.hand.split()
        other = str(other).split()
        my_points = 0
        opponent_points = 0
        my_points += self.hand_suit(self.hand)
        opponent_points += self.hand_suit(other)
        if self.combinate(self.hand) > my_points:
            my_points = self.combinate(self.hand)
        if self.combinate(other) > opponent_points:
            opponent_points = self.combinate(other)
        if self.sort_hand(self.hand) > my_points:
            my_points = self.sort_hand(self.hand)
        if self.sort_hand(other) > opponent_points:
            opponent_points = self.sort_hand(other)
        if self.straight_flush(self.hand) > my_points:
            my_points = self.straight_flush(self.hand)
        if self.straight_flush(other) > opponent_points:
            opponent_points = self.straight_flush(other)
        print(my_points)
        print(opponent_points)
        if my_points > opponent_points:
            return "Win"
        elif my_points < opponent_points:
            return "Loss"
        else:
            return self.kicker(self.hand, other)


player = PokerHand("6S AD 7H 4S AS")
other = PokerHand("AH AC 5H 6H 7S")
print(player.compare_with(other))
