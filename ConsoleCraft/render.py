import os
import sys
from world import World
from entity import Entity


def enable_vt100() -> None:
    if os.name == "nt":
        os.system("")


def setup() -> None:
    enable_vt100()


def set_colour(colour : str) -> None:
    colours = { #Set of tuples representing colours
    # Tuples are in format: (colour_code, style)
    # Style will either be 0 or 1, affecting whether it's regular or bright
        "black": (30, 0),
        "red": (31, 0),
        "green": (32, 0),
        "brown": (33, 0),
        "blue": (34, 0),
        "purple": (35, 0),
        "cyan": (36, 0),
        "gray": (37, 0),
        "dark gray": (30, 1),
        "bright red": (31, 1),
        "bright green": (32, 1),
        "yellow": (33, 1),
        "bright blue": (34, 1),
        "bright magenta": (35, 1),
        "bright cyan": (36, 1),
        "white": (37, 1)
    }

    sys.stdout.write(f"\033[{colours[colour][1]};{colours[colour][0]}m")


def set_cursor(x : int, y : int) -> None:
    sys.stdout.write(f"\033[{y};{x}H")


def print_at(x : int, y : int, msg : str) -> None:
    set_cursor(x, y)
    print(msg)


def print_map(world : World, camera : Entity) -> None:
    for y in range(20):
        line = ""
        for x in range(80):
            tile_data = world.get_tile_data(x + camera.x, y + camera.y)
            set_colour(tile_data["colour"])
            line += tile_data["char"]
        print_at(1, y + 1, line)