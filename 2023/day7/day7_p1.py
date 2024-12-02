from dataclasses import dataclass
from collections import Counter
from enum import Enum
from functools import total_ordering
from pprint import PrettyPrinter

pp = PrettyPrinter(indent=4)


def get_text():
    with open("day7/input.txt") as f:
        return f.readlines()


@total_ordering
class HandType(Enum):
    FIVEOFAKIND = 6
    FOUROFAKIND = 5
    FULLHOUSE = 4
    THREEOFAKIND = 3
    TWOPAIR = 2
    ONEPAIR = 1
    HIGHCARD = 0

    def __lt__(self, other):
        if self.__class__ is other.__class__:
            return self.value < other.value
        return NotImplemented


cardorder = {
    "A": 12,
    "K": 11,
    "Q": 10,
    "J": 9,
    "T": 8,
    "9": 7,
    "8": 6,
    "7": 5,
    "6": 4,
    "5": 3,
    "4": 2,
    "3": 1,
    "2": 0,
}


@total_ordering
@dataclass
class Hand:
    hand: str
    bid: int
    count_of_cards: Counter | None = None
    type: HandType | None = None
    rank: int | None = None

    def __lt__(self, other):
        if self.__class__ is other.__class__:
            if self.type == other.type:
                for own_card, other_card in zip(self.hand, other.hand):
                    if own_card == other_card:
                        continue
                    return cardorder[own_card] < cardorder[other_card]
            return self.type < other.type
        return NotImplemented

    def _get_first(self):
        self.first_card = self.hand[0]

    def _get_count_of_cards(self):
        self.count_of_cards = Counter(self.hand)

    def _get_type(self):
        cards = self.count_of_cards.most_common()
        first_cards = cards[0][1]
        if len(cards) > 1:
            second_cards = cards[1][1]
        if first_cards == 5:
            self.type = HandType.FIVEOFAKIND
        elif first_cards == 4:
            self.type = HandType.FOUROFAKIND
        elif first_cards == 3 and second_cards == 2:
            self.type = HandType.FULLHOUSE
        elif first_cards == 3:
            self.type = HandType.THREEOFAKIND
        elif first_cards == 2 and second_cards == 2:
            self.type = HandType.TWOPAIR
        elif first_cards == 2:
            self.type = HandType.ONEPAIR
        else:
            self.type = HandType.HIGHCARD

    def calc_all(self):
        self._get_first()
        self._get_count_of_cards()
        self._get_type()

    def calc_winnings(self):
        return self.rank * self.bid


def main():
    lines = get_text()
    hands = []
    for line in lines:
        hands.append(Hand(hand=line.split()[0], bid=int(line.split()[1])))

    for hand in hands:
        hand.calc_all()

    hands.sort()

    winnings = []
    for rank, hand in enumerate(hands, start=1):
        hand.rank = rank
        winnings.append(hand.calc_winnings())

    pp.pprint(sum(winnings))


if __name__ == "__main__":
    main()
