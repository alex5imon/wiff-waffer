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

    def __init__(self, screen):
        self._screen = screen
        self._menu = Menu(50, 50, 20, 5, 'vertical', 100, screen,
                          [('Create Player', 1, None),
                           ('Choose Existent Player', 2, None)])

        self._menu.set_center(True, True)
        self._menu.set_alignment('center', 'center')
        self._state = 0
        self._prev_state = 1
        self._rect_list = []

    def on_init(self):
        print "players"
        menu_list = []
        players = m.get_players()
        i = 1
        for p in players:
            menu_list.append((p._name, i, None))
            i += 1
            if i >= 10:
                break
        menu_list.append(("Next page", i, None))
        self._menu = Menu(50, 50, 20, 5, 'vertical', 100, self._screen, menu_list)

    def on_event(self, event):
        if event.type == pygame.KEYDOWN or event.type == EVENT_CHANGE_STATE:
            if self._state == 0:
                self._rect_list, self._state = self._menu.update(event, self._state)
            else:
                # TODO: add the player to match and go back
                m.on_change_menu('match')  # Go to match
            if self._state == 1:
                m.on_change_menu('add')  # Go to create player
            if self._state == 2:
                m.on_change_menu('choose')  # Go to choose player
            self._state = 0
            # Go back
            if event.key == pygame.K_ESCAPE:
                m.on_change_menu('match')  # Go to match

    def on_loop(self):
        if self._prev_state != self._state:
            pygame.event.post(pygame.event.Event(EVENT_CHANGE_STATE, key=0))
            self._prev_state = self._state

    def on_render(self):
        # Render the screen
        pygame.display.update(self._rect_list)

