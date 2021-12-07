from lib.card import Card
from typing import Optional

class VictoryPile:
    def __init__(self):
        # We only need to know the top card, the rest under it don't matter
        self.top_card: Optional[Card] = None

    def play(self, card: Card):
        if self.put_allowed(card):
            self.top_card = card

    def put_allowed(self, card: Card) -> bool:
        if self.top_card is None:
            return card.value == 1

        # suits match and card is one higher than previous
        if self.top_card.suit == card.suit and card.value == self.top_card.value + 1:
            return True

        return False
