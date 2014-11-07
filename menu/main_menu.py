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


class MainMenu:

    def __init__(self, screen):
        self._menu = Menu(50, 50, 20, 5, 'horizontal', 100, screen,
                          [('Single Game', 1, None),
                           ('Tournament', 2, None)])

        self._menu.set_background(screen, "assets/backgrounds/main_menu.png")

        self._menu.set_center(True, True)
        self._menu.set_alignment('center', 'center')
        self._state = 0
        self._prev_state = 1
        self._rect_list = []

    def on_init(self):
        m.reset_game()

    def on_event(self, event):
        if event.type == pygame.KEYDOWN or event.type == EVENT_CHANGE_STATE:
            if self._state == 0:
                self._rect_list, self._state = self._menu.update(event, self._state)
            if self._state == 1:
                m.on_change_menu('match')
                self._state = 0
            else:
                self._state = 0

    def on_loop(self):
        if self._prev_state != self._state:
            pygame.event.post(pygame.event.Event(EVENT_CHANGE_STATE, key=0))
            self._prev_state = self._state

    def on_render(self):
        # Render the screen
        pygame.display.update(self._rect_list)

