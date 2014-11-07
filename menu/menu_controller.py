#!/usr/bin/env python

# __main__.py
#
# Copyright (C) 2014 Alejandro Simon
# License: http://www.gnu.org/licenses/gpl-2.0.txt GNU General Public License v2
#

import pygame
import main_menu
import tournament_menu
import match_menu
import add_menu
import player_menu
import choose_menu
import avatar_menu
import colour_menu
from utils import EVENT_CHANGE_STATE


class MenuController:
    def __init__(self, screen):

        self._screen = screen
        self._state = 0
        # Create diccionary of menus
        self._menu_list = {}
        self._menu_list['main'] = main_menu.MainMenu(screen)
        self._menu_list['tournament'] = tournament_menu.TournamentMenu(screen)
        self._menu_list['add'] = add_menu.AddMenu(screen, 'match')
        self._menu_list['player1'] = player_menu.PlayerMenu(screen, 1, 'match')
        self._menu_list['player2'] = player_menu.PlayerMenu(screen, 2, 'match')
        self._menu_list['player_tournament'] = player_menu.PlayerMenu(screen, 1, 'tournament')
        self._menu_list['match'] = match_menu.MatchMenu(screen)
        self._menu_list['choose'] = choose_menu.ChooseMenu(screen)
        self._menu_list['avatar'] = avatar_menu.AvatarMenu(screen, 'match')
        self._menu_list['colour'] = colour_menu.ColourMenu(screen, 'match')
        # Current menu
        self._current = self._menu_list['main']

    def on_event(self, event):
        self._current.on_event(event)

    def on_loop(self):
        self._current.on_loop()

    def on_render(self):
        self._current.on_render()

    def on_change_menu(self, menu):
        try:
            self._current = self._menu_list[menu]
            self._current.on_init()
        except:
            print 'ERROR: passed %s' % menu
            self._current = self._menu_list['main']
        pygame.event.post(pygame.event.Event(EVENT_CHANGE_STATE, key=0))

