#!/usr/bin/env python

# colour_menu.py
#
# Copyright (C) 2014 Alejandro Simon
# License: http://www.gnu.org/licenses/gpl-2.0.txt GNU General Public License v2
#

import pygame
import __main__ as m
from menu import Menu
import utils as u


class ColourMenu:

    def __init__(self, screen):
        self._menu = Menu(50, 50, 20, 5, 'horizontal', 100, screen,
                          [('Image', 1, u.red_image),
                           ('Image', 2, u.blue_image),
                           ('Image', 3, u.green_image),
                           ('Image', 4, u.yellow_image),
                           ('Image', 5, u.white_image)], "assets/backgrounds/color_menu.png")

        self._menu.set_center(True, True)
        self._menu.set_alignment('center', 'center')
        self._state = 0
        self._prev_state = 1
        self._rect_list = []

    def on_init(self):
        pass

    def on_event(self, event):
        if event.type == pygame.KEYDOWN or event.type == u.EVENT_CHANGE_STATE:
            colour_selected = None
            if self._state == 0:
                self._rect_list, self._state = self._menu.update(event, self._state)
            if event.key == pygame.K_RETURN:
                if self._state == 1:
                    colour_selected = u.RED
                elif self._state == 2:
                    colour_selected = u.BLUE
                elif self._state == 3:
                    colour_selected = u.GREEN
                elif self._state == 4:
                    colour_selected = u.YELLOW
                elif self._state == 5:
                    colour_selected = u.WHITE
                if colour_selected is not None:
                    m.create_player(colour=colour_selected)
                    m.on_change_menu('match')
            self._state = 0
            # Go back
            if event.key == pygame.K_ESCAPE:
                m.on_change_menu('match')  # Go to create player

    def on_loop(self):
        if self._prev_state != self._state:
            pygame.event.post(pygame.event.Event(u.EVENT_CHANGE_STATE, key=0))
            self._prev_state = self._state

    def on_render(self):
        # Render the screen
        pygame.display.update(self._rect_list)
