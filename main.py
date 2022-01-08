#!/usr/bin/env python

import pprint
import pygame
from pygame.locals import *
import sys

from game.table import CardTable
from lib.card import Card


#
# print(table.devils_six)
# print(table.play_piles)
# # print(table.draw_pile)
# # pprint.pprint(table.possible_moves())
#
# print(table.play_piles)

def main():
    table = CardTable()
    table.deal()
    pygame.init()
    screen = pygame.display.set_mode((900, 700))
    pygame.display.set_caption('Churchill')
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((25, 100, 25))

    screen.blit(background, (0, 0))

    card = table.play_piles[0].top_card
    pretty_card = card.sprite
    pretty_card.rect.center = screen.get_rect().center
    group = pygame.sprite.Group(pretty_card)
    group.draw(screen)

    pygame.display.update()
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                return

        # screen.blit(background, (0, 0))
        # card_images = load_card_images()
        #
        # surf.blit(card_images, (100, 100))
        # pygame.display.flip()



if __name__ == '__main__': main()
