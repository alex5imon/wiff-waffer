#!/usr/bin/env python

# __main__.py
#
# Copyright (C) 2014 Alejandro Simon
# License: http://www.gnu.org/licenses/gpl-2.0.txt GNU General Public License v2
#

import pygame
import __main__ as m
from menu import Menu
from utils import EVENT_CHANGE_STATE


class ChooseMenu:

    def __init__(self, screen, previous):
        self._previous = previous
        self._screen = screen
        self._menu = None
        self._menu_list = []
        self._state = 0
        self._prev_state = 1
        self._rect_list = []

    def on_init(self):
        players = m.get_players()
        i = 1
        for p in players:
            self._menu_list.append((p._name, i, None))
            i += 1
            if i >= 10:
                break
        self._menu_list.append(("Next page", i, None))
        self._menu = Menu(50, 50, 20, 5, 'vertical', 100, self._screen, self._menu_list, "assets/backgrounds/choose_menu.png")
        self._menu.set_center(True, True)
        self._menu.set_alignment('center', 'center')

    def on_event(self, event):
        if event.type == pygame.KEYDOWN or event.type == EVENT_CHANGE_STATE:
            if self._state == 0:
                self._rect_list, self._state = self._menu.update(event, self._state)
            else:
                player_name = self._menu_list[self._state - 1][0]
                if self._previous == 'tournament':
                    m.add_player_by_name(player_name, tournament=True)
                else:
                    m.add_player_by_name(player_name, tournament=False)
                m.on_change_menu(self._previous)  # Go to match
                self._state = 0
                del self._menu_list[:]
            # Go back
            if event.key == pygame.K_ESCAPE:
                m.on_change_menu(self._previous)  # Go to match

    def on_loop(self):
        if self._prev_state != self._state:
            pygame.event.post(pygame.event.Event(EVENT_CHANGE_STATE, key=0))
            self._prev_state = self._state

    def on_render(self):
        # Render the screen
        pygame.display.update(self._rect_list)

