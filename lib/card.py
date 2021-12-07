from enum import Enum, auto

class Card:
    class Suit(Enum):
        HEARTS = auto()
        DIAMONDS = auto()
        CLUBS = auto()
        SPADES = auto()

    class SuitIcon(Enum):
        HEARTS = 'h'  # "♥h"
        DIAMONDS = 'd'  # "♦d"
        CLUBS = 'c'  # "♣c"
        SPADES = 's'  # "♠s"

    class FaceCard(Enum):
        JACK = 11
        QUEEN = 12
        KING = 13
        ACE = 1

    class Color(Enum):
        RED = auto()
        BLACK = auto()

    def __init__(self, suit: Suit, value: int):
        self.suit = self.Suit(suit)
        self.value = value
        self.face_up = False

    def __str__(self):
        if not self.face_up:
            return "?"
        if self.is_facecard:
            return f"{self.FaceCard(self.value).name[0]}{self.suit_icon}"
        else:
            return f"{self.value}{self.suit_icon}"

    def __repr__(self):
        return self.__str__()

    def turn(self):
        self.face_up = not self.face_up

    @staticmethod
    def chr(letter: str) -> Suit:
        if letter == 's': return Card.Suit.SPADES
        if letter == 'h': return Card.Suit.HEARTS
        if letter == 'd': return Card.Suit.DIAMONDS
        if letter == 'c': return Card.Suit.CLUBS

        raise ValueError(f"Unknown suit {letter}")

    @property
    def suit_name(self):
        return self.suit.name

    @property
    def suit_icon(self):
        return self.SuitIcon[self.suit.name].value

    @property
    def color(self):
        if self.suit == self.Suit.HEARTS or self.suit == self.Suit.DIAMONDS:
            return self.Color.RED
        else:
            return self.Color.BLACK

    @property
    def is_facecard(self):
        try:
            self.FaceCard(self.value)
            return True
        except ValueError:
            return False
