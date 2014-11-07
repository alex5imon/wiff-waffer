#!/usr/bin/env python

# utils.py
#
# # Copyright (C) 2014 Alejandro Simon
# License: http://www.gnu.org/licenses/gpl-2.0.txt GNU General Public License v2
#

import os
import json
import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

## This is a user event that should be sent whenever the game state is changed
#  (at the main game loop level)
EVENT_CHANGE_STATE = pygame.USEREVENT + 1


def is_gui():
    return 'DISPLAY' in os.environ


def ensure_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)


def read_file_contents(path):
    if os.path.exists(path):
        with open(path) as infile:
            return infile.read().strip()


def write_file_contents(path, data):
    with open(path, 'w') as outfile:
        outfile.write(data)


def read_json(filepath, silent=True):
    try:
        return json.loads(read_file_contents(filepath))
    except Exception:
        if not silent:
            raise


def write_json(filepath, data, sort_keys=True):
    with open(filepath, 'w') as outfile:
        json.dump(data, outfile, indent=2, sort_keys=sort_keys)


def load_image(file_name, folder, colorkey=None):
    full_name = os.path.join(folder, file_name)
    try:
        image = pygame.image.load(full_name)
    except:
        print 'Cannot load image:', full_name
    '''
    image = image.convert_alpha()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, pygame.RLEACCEL)
    '''
    return image


avatar_1 = load_image("1.png", "assets/avatars")
avatar_2 = load_image("2.png", "assets/avatars")
avatar_3 = load_image("3.png", "assets/avatars")
avatar_4 = load_image("4.png", "assets/avatars")
avatar_5 = load_image("5.png", "assets/avatars")

red_image = load_image("red.png", "assets/colours")
blue_image = load_image("blue.png", "assets/colours")
green_image = load_image("green.png", "assets/colours")
yellow_image = load_image("yellow.png", "assets/colours")
white_image = load_image("white.png", "assets/colours")


def string_to_avatar(image):
    if image == "1.png":
        return avatar_1
    elif image == "2.png":
        return avatar_2
    elif image == "3.png":
        return avatar_3
    elif image == "4.png":
        return avatar_4
    elif image == "5.png":
        return avatar_5

def set_background(screen, asset_path):
    screensize = screen.get_rect()

    background = pygame.transform.scale(
        pygame.image.load(asset_path),
        (screensize.width, screensize.height))

    screen.blit(background, background.get_rect())