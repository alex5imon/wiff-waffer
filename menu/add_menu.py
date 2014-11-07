#!/usr/bin/env python

# __main__.py
#
# Copyright (C) 2014 Alejandro Simon
# License: http://www.gnu.org/licenses/gpl-2.0.txt GNU General Public License v2
#

import pygame
import eztext
import __main__ as m
from utils import EVENT_CHANGE_STATE

user_name = None
user_colour = None
user_avatar = None


class AddText:

    def __init__(self, screen):
        self._screen = screen
        self._txt = eztext.Input(x=50, y=50, maxlength=45, color=(255, 0, 0), prompt='User name: ')

    def on_event(self, event):
        self._txt.update(event)

    def on_render(self):
        # blit txtbx on the sceen
        self._txt.draw(self._screen)

    def on_reset(self):
        self._txt.value = ''

    def get_name(self):
        return self._txt.value


class AddMenu:

    def __init__(self, screen, previous):
        self._screen = screen
        self._previous = previous

        self._state = 0
        self._ready = False
        self._prev_state = 1
        self._rect_list = []
        self._addText = AddText(screen)

    def on_init(self):
        pass

    def on_event(self, event):

        if event:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                self._state = 0
                m.create_player(name=self._addText.get_name())
                pygame.event.post(pygame.event.Event(EVENT_CHANGE_STATE, key=0))
                # m.clear_screen()
                m.on_change_menu('avatar')
                self._addText.on_reset()
            else:
                self._addText.on_event(event)
                # Go back
                if event.key == pygame.K_ESCAPE:
                    m.on_change_menu(self._previous)
                    self._mode = 0

    def on_loop(self):
        if self._prev_state != self._state:
            pygame.event.post(pygame.event.Event(EVENT_CHANGE_STATE, key=0))
            self._prev_state = self._state
        self._ready = m.get_current_player().is_player_complete()

    def on_render(self):
        # Render text
        self._addText.on_render()
