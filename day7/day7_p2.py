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
    "T": 9,
    "9": 8,
    "8": 7,
    "7": 6,
    "6": 5,
    "5": 4,
    "4": 3,
    "3": 2,
    "2": 1,
    "J": 0,
}


@total_ordering
@dataclass
class Hand:
    hand: str
    bid: int
    count_of_cards: Counter | None = None
    jokers: int = 0
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
        self.jokers = self.count_of_cards["J"]

    def _get_type(self):  # remove J from count_of_cards!!!
        self.count_of_cards["J"] = 0
        cards = self.count_of_cards.most_common()
        first_cards = cards[0][1]
        first_cards_with_jokers = first_cards + self.jokers
        if len(cards) > 1:
            second_cards = cards[1][1]
            first_and_second_with_jokers = first_cards_with_jokers + second_cards
        else:
            first_and_second_with_jokers = 0
        if first_cards_with_jokers == 5:
            self.type = HandType.FIVEOFAKIND
        elif first_cards_with_jokers == 4:
            self.type = HandType.FOUROFAKIND
        elif first_and_second_with_jokers == 5:
            self.type = HandType.FULLHOUSE
        elif first_cards_with_jokers == 3:
            self.type = HandType.THREEOFAKIND
        elif first_and_second_with_jokers == 4:
            self.type = HandType.TWOPAIR
        elif first_cards_with_jokers == 2:
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

    pp.pprint(hands)

    winnings = []
    for rank, hand in enumerate(hands, start=1):
        hand.rank = rank
        winnings.append(hand.calc_winnings())

    pp.pprint(sum(winnings))


if __name__ == "__main__":
    main()
