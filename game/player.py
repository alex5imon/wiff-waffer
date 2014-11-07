#!/usr/bin/env python

# __main__.py
#
# Copyright (C) 2014 Alejandro Simon
# License: http://www.gnu.org/licenses/gpl-2.0.txt GNU General Public License v2
#

import os.path
import pygame
import utils as u


class Player:

    def __init__(self, name, avatar, avatar_name, colour):

        # Created by user
        self._name = name
        self._avatar = avatar
        self._avatar_name = avatar_name
        self._colour = colour
        # Statistics
        self._games_played = 0
        self._games_won = 0

    def is_player_complete(self):
        return not (self._name is None or self._avatar is None or self._colour is None)

    def game_played(self):
        self._games_played += 1

    def game_won(self):
        self._games_won += 1

    def load(self, filename):
        data = u.read_json(filename)
        if data is not None:
            self._name = data[0]['name']
            self._avatar = u.string_to_avatar(data[0]['avatar_name'])
            self._avatar_name = data[0]['avatar_name']
            self._colour = data[0]['colour']
        else:
            print "Error loading %s" % filename

    def save(self):
        data = [{'name': self._name, 'avatar_name': self._avatar_name, 'colour': self._colour}]
        path = os.path.join("players", "%s.json" % self._name)
        u.write_json(path, data, sort_keys=True)

    def render(self, screen, left=True):
        position = None
        if left:
            position = (10, 50)
        else:
            position = (500, 50)
        # Draw avatar
        if self._avatar is not None:
            screen.blit(self._avatar, position)
        # Draw name
        if left:
            position = (10, 80)
        else:
            position = (480, 80)
        if self._name is not None:
            msg = "Name: %s" % self._name
        else:
            msg = "Unknown"
        text = pygame.font.Font(None, 32).render(msg, 1, self._colour)
        screen.blit(text, position)

