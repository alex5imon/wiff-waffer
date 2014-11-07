#!/usr/bin/env python

# __main__.py
#
# Copyright (C) 2014 Alejandro Simon
# License: http://www.gnu.org/licenses/gpl-2.0.txt GNU General Public License v2
#

import pygame
#from pygame.locals import *
import utils as u
import sys
import menu.menu_controller as mc
import game.game_controller as gc


class WiffWaffer:
    def __init__(self):
        self._state = 0
        self._running = True
        self._display_surf = None
        self._clear_screen = False
        self.size = self.weight, self.height = 640, 400

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        pygame.display.set_caption("Wiff Waffer")

        # Ignore mouse motion (greatly reduces resources when not needed)
        pygame.event.set_blocked(pygame.MOUSEMOTION)

        # create the pygame clock
        self._clock = pygame.time.Clock()
        self._running = True

        # Create menu
        self._menu_controller = mc.MenuController(self._display_surf)

        # Create game
        self._game_controller = gc.GameController(self._display_surf)
        self._game_controller.on_load()

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
        if self._state == 0:
            self._menu_controller.on_event(event)
        elif self._state == 1:
            self._game_controller.on_event(event)

    def on_loop(self):
        if self._state == 0:
            self._menu_controller.on_loop()
        elif self._state == 1:
            self._game_controller.on_loop()

    def on_render(self):
        # Render
        if self._state == 0:
            self._menu_controller.on_render()
        elif self._state == 1:
            self._game_controller.on_render()
        # Clear screen
        if self._clear_screen:
            self._display_surf.fill((u.BLACK))
            pygame.display.update()
            self._clear_screen = False
        # refresh the display
        pygame.display.flip()

    def on_cleanup(self):
        pygame.quit()
        sys.exit()

    def on_execute(self):
        if self.on_init() is False:
            self._running = False

        while(self._running):

            # make sure the program is running at 30 fps
            self._clock.tick(30)
            # Update
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            # Render
            self.on_render()
        self.on_cleanup()


game = None


def clear_screen():
    game._clear_screen = True


def on_change_menu(menu):
    game._menu_controller.on_change_menu(menu)
    clear_screen()


def back_to_menu():
    game._state = 0
    on_change_menu('main')
    clear_screen()


def start_game():
    game._state = 1
    clear_screen()


def create_player(name=None, avatar=None, colour=None):
    game._game_controller.create_player(name, avatar, colour)


def add_player_by_name(name=None):
    game._game_controller.add_player_by_name(name)


def get_current_player():
    return game._game_controller._currentPlayer


def get_player_1():
    return game._game_controller._player1


def get_player_2():
    return game._game_controller._player2


def get_players():
    return game._game_controller._players


def reset_game():
    game._game_controller.on_reset()

# Program begins
if __name__ == "__main__":

    if not u.is_gui():
        sys.exit("wiff-waffer requires an X session")

    u.ensure_dir("players")

    game = WiffWaffer()
    game.on_execute()
