#!/usr/bin/env python

# player.py
#
# Copyright (C) 2014 Alejandro Simon
# License: http://www.gnu.org/licenses/gpl-2.0.txt GNU General Public License v2
#

import pygame
import match
from random import randint
import player as p
import utils as u


class TournamentController:

    def __init__(self, screen):
        self._screen = screen
        self.on_reset()

    def on_load(self):
        pass

    def on_event(self, event):
        self.self._matches[self._currentMatch].on_event(event)

    def on_loop(self):
        self.self._matches[self._currentMatch].on_loop()

    def on_render(self):
        self.self._matches[self._currentMatch].on_render()

    def on_reset(self):
        self._currentMatch = 0
        self._matches = []
        for m in range(0, 8):
            self._matches.append(match.Match(self._screen,
                                             p.Player("Unknown", None, None, None),
                                             p.Player("Unknown", None, None, None)))
        self._num_players = 0

    def draw_table(self):
        # Match 1
        text = pygame.font.Font(None, 32).render(self._matches[0]._player1._name, 1, (0, 255, 0))
        self._screen.blit(text, (50, 50))
        text = pygame.font.Font(None, 32).render(self._matches[0]._player2._name, 1, (0, 255, 0))
        self._screen.blit(text, (50, 80))
        # Match 2
        text = pygame.font.Font(None, 32).render(self._matches[1]._player1._name, 1, (0, 255, 0))
        self._screen.blit(text, (50, 200))
        text = pygame.font.Font(None, 32).render(self._matches[1]._player2._name, 1, (0, 255, 0))
        self._screen.blit(text, (50, 230))
        # Match 3
        text = pygame.font.Font(None, 32).render(self._matches[2]._player1._name, 1, (0, 255, 0))
        self._screen.blit(text, (400, 50))
        text = pygame.font.Font(None, 32).render(self._matches[2]._player2._name, 1, (0, 255, 0))
        self._screen.blit(text, (400, 80))
        # Match 4
        text = pygame.font.Font(None, 32).render(self._matches[3]._player1._name, 1, (0, 255, 0))
        self._screen.blit(text, (400, 200))
        text = pygame.font.Font(None, 32).render(self._matches[3]._player2._name, 1, (0, 255, 0))
        self._screen.blit(text, (400, 230))
        # Match 5
        # Match 6
        # Match 7
        # Match 8
        # Match 9

    def add_player(self, player):
        if not self.is_full():
            while True:
                idx = randint(0, 7)
                if self._matches[idx]._player1._avatar is None:
                    self._matches[idx]._player1 = player
                    self._num_players += 1
                    return
                elif self._matches[idx]._player2_avatar is None:
                    self._matches[idx]._player2 = player
                    self._num_players += 1
                    return

    def add_player_by_name(self, name, players):
        for p in players:
            if p._name == name:
                self.add_player(p)
                return

    def create_player(self, name=None, avatar=None, colour=None):
        if name is not None:
            self._currentPlayer._name = name
        if avatar is not None:
            self._currentPlayer._avatar = u.string_to_avatar(avatar)
            self._currentPlayer._avatar_name = avatar
        if colour is not None:
            self._currentPlayer._colour = colour
        if self._currentPlayer.is_player_complete():
            self._players.append(self._currentPlayer)
            self._currentPlayer.save()
            self.add_player()
            return True
        return False

    def start_tournament(self):
        self._currentMatch = self._matches[0]

    def is_full(self):
        return self._num_players >= 8
