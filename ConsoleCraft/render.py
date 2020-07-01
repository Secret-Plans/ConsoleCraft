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

    return f"\033[{colours[colour][1]};{colours[colour][0]}m"


def clear_line(line : int) -> None:
    set_cursor(1, line)
    print(" " * 120)
    set_cursor(1, line)


def set_cursor(x : int, y : int) -> None:
    sys.stdout.write(f"\033[{y};{x}H")


def print_at(x : int, y : int, msg : str) -> None:
    set_cursor(x, y)
    print(msg)


def print_map(world : World, entities : list, camera : Entity) -> None:
    for y in range(20):
        actual_y = y + camera.y - 10
        line = ""
        for x in range(80):
            actual_x = x + camera.x - 40
            no_entity_on_tile = True
            for entity in entities:
                if actual_x == entity.x and actual_y == entity.y and entity.visible:
                    no_entity_on_tile = False
                    line += set_colour(entity.colour)
                    line += entity.char
                    break
            if no_entity_on_tile:
                tile_data = world.get_tile_data(actual_x, actual_y)
                line += set_colour(tile_data["colour"])
                line += tile_data["char"]
        print_at(1, y + 1, line)