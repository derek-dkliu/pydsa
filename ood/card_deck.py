import random
from enum import Enum

class Suit(Enum):
    DIAMOND = '♦'
    ClUB = '♣'
    HEART = '♥'
    SPADE = '♠'

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def value(self):
        return self.rank

    def __str__(self):
        return f"{self.suit.value}{self.rank:<2}"

class Deck:
    def __init__(self):
        self.next = 0
        self.cards = []

    @staticmethod
    def create(cardtype):
        deck = Deck()
        for suit in Suit:
            for rank in range(1, 14):
                deck.cards.append(cardtype(suit, rank))
        return deck

    def shuffle(self):
        # length = len(self.cards)
        # for i in range(length):
        #     r = random.randint(i, length - 1)
        #     self.cards[i], self.cards[r] = self.cards[r], self.cards[i]
        random.shuffle(self.cards)
        self.next = 0

    def deal_card(self):
        if self.next >= len(self.cards):
            raise Exception("Deck is empty")
        card = self.cards[self.next]
        self.next += 1
        return card

    def deal_hand(self, num):
        if self.get_remaining() < num:
            raise Exception("Not enough cards left")
        start = self.next
        self.next += num
        return self.cards[start:self.next]

    def get_remaining(self):
        return len(self.cards) - self.next

    def __len__(self):
        return len(self.cards)

    def __str__(self):
        length = len(self.cards)
        size = length // 4
        groups = [f"total: {length}"]
        group = []
        for i in range(length):
            group.append(self.cards[i])
            if size == len(group) or i == length - 1:
                groups.append(' '.join(map(str, group)))
                group = []
        return '\n'.join(groups)

class Hand:
    def __init__(self):
        self.cards = []

    def score(self):
        return sum(map(lambda c:c.value(), self.cards))

    def add_card(self, card):
        self.cards.append(card)

    def __str__(self):
        return ' '.join(map(str, self.cards))

class BlackJackHand(Hand):
    def score(self):
        scores = [0]
        for card in self.cards:
            values = card.value()
            if isinstance(values, list):
                length = len(scores)
                scores *= len(values)
                for i, val in enumerate(values):
                    for j in range(length):
                        scores[i * length + j] += val
            else:
                for i in range(len(scores)):
                    scores[i] += card.value()
        max = 0
        min = float('inf')
        for score in scores:
            if score <= 21 and score > max:
                max = score
            elif score > 21 and score < min:
                min = score
        return max if max > 0 else min

    def is21(self):
        return self.score() == 21

    def is_busted(self):
        return self.score() > 21

    def is_blackjack(self):
        return len(self.cards) == 2 and \
                (self.cards[0].value() == 10 and self.cards[1].value() == 1) or \
                (self.cards[0].value() == 1 and self.cards[1].value() == 10)

class BlackJackCard(Card):
    def value(self):
        if self.is_ace():
            return [1, 11]
        elif self.is_face():
            return 10
        else:
            return self.rank

    def is_ace(self):
        return self.rank == 1

    def is_face(self):
        return self.rank >= 11 and self.rank <= 13

# deck = Deck.create(Card)
# deck.shuffle()
# hand = Hand()
# for card in deck.deal_hand(5):
#     hand.add_card(card)
# print(hand)

deck = Deck.create(BlackJackCard)
deck.shuffle()
hand = BlackJackHand()
while True:
    hand.add_card(deck.deal_card())
    if hand.is21() or hand.is_busted():
        break
print(hand.score(), hand)
