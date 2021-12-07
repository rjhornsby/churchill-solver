from lib.card import Card
from lib.stack import CardStack


class PlayPile(CardStack):

    def __init__(self, initial_size):
        super().__init__()
        self.initial_size = initial_size

    # @property
    def initial_size(self) -> int:
        return self.initial_size

    @property
    def initial_stack_full(self) -> bool:
        return len(self) == self.initial_size

    # is this card (or this stack of cards) allowed to be picked up?
    def get_allowed(self, position: int) -> bool:
        # No cards here
        if len(self) == 0:
            return False

        if not self[position].face_up:
            return False

        # last/only card
        if position == len(self) - 1:
            return True

        # a set of cards must be in sequence
        for i in range(position, len(self) - 2):
            # same color not allowed
            if self[i].color == self[i+1].color:
                return False
            # cards must be in numerical order
            if not self[i].value == self[i+1].value - 1:
                return False

        return True

    def put_allowed(self, moving_card: Card) -> bool:
        # only kings can be moved onto empty play piles
        if len(self) == 0:
            return moving_card.value == Card.FaceCard.KING

        # moving_card must be one less than destination_card, and not same color
        if self[-1].color == moving_card.color:
            return False

        if not self[-1].value == moving_card.value + 1:
            return False

        return True
