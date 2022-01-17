import random
import pickle
import json
from lib.card import Card
from lib.stack import CardStack


class Deck(CardStack):
    GAME_NUMBER = "002"

    def __init__(self, num_standard_decks=1):
        super().__init__()
        self.load_dealpack()
        # try:
        #     self.load()
        # except FileNotFoundError:
        #     self.create(num_standard_decks)
        #     self.shuffle()
        #     self.store()

    def create(self, num_standard_decks):
        for _ in range(num_standard_decks):
            for suit in Card.Suit.__members__.values():
                for value in range(1, 14):
                    self.append(Card(suit, value))

    def load_dealpack(self):
        with open('assets/deal_packs/dealpack_1.json') as fh:
            data = json.load(fh)
            cards = data[int(self.GAME_NUMBER) - 1]['cards']
            print(cards)
            for card in cards:
                self.append(Card(Card.chr(card['suit']), card['value']))
            print(f"loaded game {self.GAME_NUMBER}")

    # def load(self):
    #     with open('/tmp/deal.pkl', 'rb') as fh:
    #         self.extend(pickle.load(fh))
    #
    # def store(self):
    #     with open('/tmp/deal.pkl', 'wb') as fh:
    #         pickle.dump(self, fh)
    #
    # def shuffle(self):
    #     random.shuffle(self)

    def is_empty(self):
        return len(self) == 0
