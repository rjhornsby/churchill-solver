from enum import Enum, auto
import pygame
from pygame.locals import *

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
        self._sprite = None

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
    def is_facecard(self) -> bool:
        try:
            self.FaceCard(self.value)
            return True
        except ValueError:
            return False

    @property
    def sprite(self) -> pygame.sprite.Sprite:
        if self._sprite is None:
            if self.is_facecard:
                self._sprite = self.Sprite(f"{self.FaceCard(self.value).name[0]}{self.suit_name[0]}")
            else:
                self._sprite = self.Sprite(f"{self.value}{self.suit_name[0]}")

        return self._sprite

    class Sprite(pygame.sprite.Sprite):
        def __init__(self, card: str):
            pygame.sprite.Sprite.__init__(self)
            card = str.upper(card)
            self.og_image = self.load_card_image(card)
            self.image = self.og_image
            self.rect = self.image.get_rect()
            self.set_rounded(15)

        def set_rounded(self, radius) -> None:
            size = self.og_image.get_size()
            rect_image = pygame.Surface(size, pygame.SRCALPHA)
            pygame.draw.rect(rect_image, (255, 255, 255), (0, 0, *size), border_radius=radius)
            self.image = self.og_image.copy().convert_alpha()
            self.image.blit(rect_image, (0, 0), None, pygame.BLEND_RGBA_MIN)

        @staticmethod
        def load_card_image(card: str) -> pygame.image:
            if len(card) != 2:
                raise ValueError('Cannot load image. Card arg must be two characters only')
            try:
                image = pygame.image.load(f"assets/card_images/{card}.png")
                image = pygame.transform.scale(image, (image.get_width() * 0.15, image.get_height() * 0.15))
            except pygame.error as message:
                print('Cannot load image')
                raise SystemExit(message)

            return image
