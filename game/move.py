from lib.stack import CardStack
from lib.card import Card
import typing

class Move:

    # We need to know which card, which stack it is in, and which stack it is going to
    # The move will need to be further calculated to determine if the card being moved
    # is taking other cards in the same stack with it
    def __init__(self, card: Card, from_stack: CardStack, to_stack: CardStack):
        super()
        self.card = card
        self.from_stack = from_stack
        self.to_stack = to_stack

    def allowed(self) -> bool:
        return self.to_stack.put_allowed(self.card)
