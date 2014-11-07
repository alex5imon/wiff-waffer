#!/usr/bin/env python

# avatar_menu.py
#
# Copyright (C) 2014 Alejandro Simon
# License: http://www.gnu.org/licenses/gpl-2.0.txt GNU General Public License v2
#

import pygame
import __main__ as m
from menu import Menu
import utils as u


class AvatarMenu:

    def __init__(self, screen, previous):
        self._screen = screen
        self._previous = previous

        self._menu = Menu(50, 50, 20, 5, 'horizontal', 100, screen,
                          [('Image', 1, u.avatar_1),
                           ('Image', 2, u.avatar_2),
                           ('Image', 3, u.avatar_3),
                           ('Image', 4, u.avatar_4),
                           ('Image', 5, u.avatar_5)], "assets/backgrounds/avatar_menu.png")

        self._menu.set_center(True, True)
        self._menu.set_alignment('center', 'center')
        self._state = 0
        self._prev_state = 1
        self._rect_list = []

    def on_init(self):
        pass

    def on_event(self, event):
        if event.type == pygame.KEYDOWN or event.type == u.EVENT_CHANGE_STATE:
            if self._state == 0:
                self._rect_list, self._state = self._menu.update(event, self._state)
            if event.key == pygame.K_RETURN:
                avatar_name = "%i.png" % self._state
                m.create_player(avatar=avatar_name)
                m.on_change_menu('colour')
            self._state = 0
            # Go back
            if event.key == pygame.K_ESCAPE:
                m.on_change_menu(self._previous)  # Go to create player

    def on_loop(self):
        if self._prev_state != self._state:
            pygame.event.post(pygame.event.Event(u.EVENT_CHANGE_STATE, key=0))
            self._prev_state = self._state

    def on_render(self):
        # Render the screen
        pygame.display.update(self._rect_list)
