#!/usr/bin/env python

import ceefax
from os.path import expanduser, join, isdir
from os import mkdir
import log_setup
from random import choice
from points import add_points
import Keyboard

if not isdir(join(expanduser('~'), '.klb')):
    mkdir(join(expanduser('~'), '.klb'))

house = choice(["Ravenclaw", "Gryffindor", "Slytherin", "Hufflepuff", "Squib",
                "Durmstrang"])

add_points(house, 1)
if house == "Hufflepuff":
    print("1 point to "+house+"! GO PUFFS!")
else:
    print("1 point to "+house+"!")

log_setup.read_from_file()


Keyboard.start_keyboard_thread()
Keyboard.subscribe(ceefax.name_page_handler)

while True:
    ceefax.loop_manager.current()
