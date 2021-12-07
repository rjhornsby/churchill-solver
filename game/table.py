from lib.card import Card
from lib.deck import Deck
from lib.stack import CardStack
from game.devils_six import DevilsSix
from game.play_pile import PlayPile
from game.victory_pile import VictoryPile


class CardTable:

    PLAY_PILE_COUNT = 10
    VICTORY_PILE_COUNT = 8
    # idx values adjusted for the array size changing as we pull cards out
    # the D6 cards start from the 6th card in the deck
    # * then the 10th card after that
    # * then the 8th card after that
    # * then the 6th card after that
    # * 4th card after that
    # * 2nd card after that
    DEVILS_SIX_IDX_LIST = [98, 88, 80, 74, 70, 68]

    def __init__(self):
        self.game_deck = None
        self.devils_six = DevilsSix()

        self.victory_piles = list()
        for _ in range(self.VICTORY_PILE_COUNT):
            self.victory_piles.append(VictoryPile())

        self.play_piles = list()
        for idx in range(self.PLAY_PILE_COUNT):
            if idx < 5: pile_size = idx + 1
            if idx == 5: pile_size = 5
            if idx > 5: pile_size = self.play_piles[idx - 1].initial_size - 1

            self.play_piles.append(PlayPile(pile_size))

        self.draw_pile = CardStack()

    def deal(self):
        self.game_deck = Deck()
        keep_dealing = True
        while keep_dealing:
            for pile_num in range(10):
                if self.play_piles[pile_num].initial_stack_full:
                    continue

                self.play_piles[pile_num].append(self.next_card())

                if len(self.game_deck) - 1 in self.DEVILS_SIX_IDX_LIST:
                    self.devils_six.append(self.next_card())
                    self.devils_six[-1].turn()

            if self.play_piles[5].initial_stack_full:
                keep_dealing = False

        # turn over the top card on each play pile
        for i in range(10):
            self.play_piles[i][-1].turn()

        # Move the remaining cards to the draw pile
        self.draw_pile = self.game_deck.copy()
        del self.game_deck

    def next_card(self):
        next_card = self.game_deck.pop()
        return next_card

    def possible_moves(self):
        moves = []
        # from devils six to victory
        for v in self.victory_piles:
            if v.put_allowed(self.devils_six.top_card):
                moves.append([self.devils_six, v])
        # from play to victory
        for p in self.play_piles:
            for v in self.victory_piles:
                if v.put_allowed(p.top_card):
                    moves.append([p, v])
                    break  # only need to find one possible victory pile slot
        # from play to play
        for p0 in self.play_piles:
            for p1 in self.play_piles:
                if p0 == p1:
                    continue
                if p1.put_allowed(p0.top_card):
                    moves.append([p0, p1, p0.top_card])

        return moves

