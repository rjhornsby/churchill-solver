from lib.card import Card


class CardStack(list[Card]):

    def __init__(self):
        super().__init__()

    @property
    def top_card(self):
        try:
            return self[-1]
        except ValueError:
            return None

    @property
    def bottom_card(self):
        try:
            return self[0]
        except ValueError:
            return None

    def put_allowed(self, _: Card):
        return NotImplemented
