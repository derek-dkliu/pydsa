from enum import Enum
import random

class Suit(Enum):
    Diamond = '♦'
    Club = '♣'
    Heart = '♥'
    Spade = '♠'

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank:>2}{self.suit.value}"

class Deck:
    def __init__(self):
        self.cards = []
        for suit in Suit:
            for i in range(13):
                self.cards.append(Card(suit, i + 1))


    def shuffle(self):
        n = len(self.cards)
        for i in range(n):
            j = int(random.random() * (i + 1))          # pick from [0, i]
            # j = i + int(random.random() * (n - i))    # pick from [i, n - 1]
            self.cards[i], self.cards[j] = self.cards[j], self.cards[i]

    def __str__(self):
        sb = []
        row = []
        for card in self.cards:
            row.append(str(card))
            if len(row) == 13:
                sb.append(' '.join(row))
                row = []
        return '\n'.join(sb) + '\n'

deck = Deck()
print(deck)
deck.shuffle()
print(deck)
