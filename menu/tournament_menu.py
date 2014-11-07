#!/usr/bin/env python

# tournament_menu.py
#
# Copyright (C) 2014 Alejandro Simon
# License: http://www.gnu.org/licenses/gpl-2.0.txt GNU General Public License v2
#

import pygame
import __main__ as m
from menu import Menu
from utils import EVENT_CHANGE_STATE


class TournamentMenu:

    def __init__(self, screen):
        self._screen = screen
        self._menu = Menu(50, 50, 20, 5, 'horizontal', 100, screen,
                          [('Add player', 1, None)])

        self._menu.set_center(True, True)
        self._menu.set_alignment('center', 'center')
        self.on_reset()

    def on_init(self):
        pass

    def on_event(self, event):
        if event.type == pygame.KEYDOWN or event.type == EVENT_CHANGE_STATE:
            if self._state == 0:
                self._rect_list, self._state = self._menu.update(event, self._state)
            if self._state == 1:
                m.on_change_menu('player_tournament')
                self._state = 0
            # Go back
            if event.key == pygame.K_ESCAPE:
                m.on_change_menu('main')  # Go to main menu
            # Play match
            if event.key == pygame.K_SPACE:
                m.start_game()  # Go to main menu

    def on_loop(self):
        if self._prev_state != self._state:
            pygame.event.post(pygame.event.Event(EVENT_CHANGE_STATE, key=0))
            self._prev_state = self._state
        self._ready = (m.get_player_1() is not None) and (m.get_player_2() is not None)

    def on_render(self):
        # Render the screen
        pygame.display.update(self._rect_list)
        # Draw players
        tournament = m.get_tournament()
        tournament.draw_table()

        if tournament.is_full():
            text = pygame.font.Font(None, 32).render("Press SPACE to start", 1, (0, 255, 0))
            self._screen.blit(text, (200, 300))

    def on_reset(self):
        self._state = 0
        self._prev_state = 1
        self._ready = False
        self._rect_list = []
