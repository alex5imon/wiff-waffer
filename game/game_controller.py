#!/usr/bin/env python

# player.py
#
# Copyright (C) 2014 Alejandro Simon
# License: http://www.gnu.org/licenses/gpl-2.0.txt GNU General Public License v2
#

import os
import match
import player as p
import utils as u


class GameController:

    def __init__(self, screen):
        self._screen = screen
        self._players = []
        self._match = None
        self._currentPlayer = p.Player("Unknown", None, None, None)
        self._playerId = 1
        # TEST
        self._player1 = None
        self._player2 = None

    def on_load(self):
        print "LOADING"
        for fn in os.listdir('players'):
            player = p.Player("Unknown", None, None, None)
            player.load(fn)
            print "name: %s" % player._name
            if os.path.isfile(fn):
                print "LADOING 2"
                print fn

    def on_event(self, event):
        self._match.on_event(event)

    def on_loop(self):
        self._match.on_loop()

    def on_render(self):
        self._match.on_render()

    def add_player_1(self, player):
        self._player1 = player

    def add_player_2(self, player):
        self._player2 = player

    def start_match(self):
        self._match = match.Match(self._screen, self._player1, self._player2)

    def create_player(self, name=None, avatar=None, colour=None):
        if name is not None:
            self._currentPlayer._name = name
        if avatar is not None:
            self._currentPlayer._avatar = u.string_to_avatar(avatar)
            self._currentPlayer._avatar_name = avatar
        if colour is not None:
            self._currentPlayer._colour = colour
        if self._currentPlayer.is_player_complete():
            if self._playerId == 1:
                self._playerId = 2
                self.add_player_1(self._currentPlayer)
            else:
                self._playerId = 1
                self.add_player_2(self._currentPlayer)
                self.start_match()
            self._players.append(self._currentPlayer)
            self._currentPlayer.save()
            self._currentPlayer = p.Player("Unknown", None, None, None)
            return True
        return False

    def get_players(self):
        return self._players

    def get_player_by_name(self, name):
        for p in self._players:
            if p._name == name:
                return p
