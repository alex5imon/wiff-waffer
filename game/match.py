#!/usr/bin/env python

# match.py
#
# Copyright (C) 2014 Alejandro Simon
# License: http://www.gnu.org/licenses/gpl-2.0.txt GNU General Public License v2
#

import pygame
import __main__ as m
import utils as u


class Match:
    def __init__(self, screen, player1, player2):

        self._screen = screen
        self.on_reset()
        self._player1 = player1
        self._player2 = player2

    def on_event(self, event):
        if event.type == pygame.KEYDOWN:
            if self._state == 0:
                if event.key == pygame.K_RETURN:
                    self._state = 1
                    u.set_background(self._screen, "assets/backgrounds/match_menu.png")
            elif self._state == 1:
                if event.key == pygame.K_RETURN:
                    self._score1 += 1
                    self.check_winner()
                    u.set_background(self._screen, "assets/backgrounds/match_menu.png")
                if event.key == pygame.K_BACKSPACE:
                    self._score2 += 1
                    self.check_winner()
                    u.set_background(self._screen, "assets/backgrounds/match_menu.png")
            elif self._state == 2 or self._state == 3:
                if event.key == pygame.K_RETURN:
                    self._state = 1
                    u.set_background(self._screen, "assets/backgrounds/match_menu.png")
            elif self._state == 4 or self._state == 5:
                if event.key == pygame.K_RETURN:
                    m.back_to_menu()

    def on_loop(self):
        pass

    def on_render(self):
        # Play to serve
        if self._state == 0:
            text = pygame.font.Font(None, 32).render("Play to serve", 1, (0, 255, 0))
            self._screen.blit(text, (50, 50))
        # Match on going
        elif self._state == 1:
            msg = "%s: %i" % (self._player1._name, self._score1)
            text = pygame.font.Font(None, 32).render(msg, 1, (0, 255, 0))
            self._screen.blit(text, (50, 50))
            msg = "%s: %i" % (self._player2._name, self._score2)
            text = pygame.font.Font(None, 32).render(msg, 1, (0, 255, 0))
            self._screen.blit(text, (50, 70))
        # Player 1 wins game
        elif self._state == 2:
            text = pygame.font.Font(None, 32).render("Player 1 wins game", 1, (0, 255, 0))
            self._screen.blit(text, (50, 50))
        # Player 2 wins game
        elif self._state == 3:
            text = pygame.font.Font(None, 32).render("Player 2 wins game", 1, (0, 255, 0))
            self._screen.blit(text, (50, 50))
        # Player 1 wins match
        elif self._state == 4:
            text = pygame.font.Font(None, 32).render("Player 1 wins match", 1, (0, 255, 0))
            self._screen.blit(text, (50, 50))
        # Player 2 wins match
        elif self._state == 5:
            text = pygame.font.Font(None, 32).render("Player 2 wins match", 1, (0, 255, 0))
            self._screen.blit(text, (50, 50))

    def on_reset(self):
        self._state = 0
        self._game1 = 0
        self._game2 = 0
        self._serve = 0
        self._player1 = None
        self._player2 = None
        self._winner = None
        self.on_reset_score()

    def on_reset_score(self):
        self._score1 = 0
        self._score2 = 0

    def check_winner(self):
        if self._score1 == 21:
            if self._game1 == 1:
                self._state = 4  # Player 1 wins match
                self._m_player1.game_played()
                self._m_player1.game_won()
                self._winner = self._player1
                self._m_player2.game_played()
                u.set_background(self._screen, "assets/backgrounds/match_menu.png")
            else:
                self._state = 2  # Player 1 wins game
                self._game1 += 1
                self.on_reset_score()
                m.clear_screen()

        if self._score2 == 21:
            if self._game2 == 1:
                self._state = 5  # Player 2 wins match
                self._m_player1.game_played()
                self._m_player2.game_played()
                self._m_player2.game_won()
                self._winner = self._player2
                m.clear_screen()
            else:
                self._state = 3  # Player 1 wins game
                self._game2 += 1
                self.on_reset_score()
                m.clear_screen()
