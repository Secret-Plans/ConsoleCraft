# Imports
import os
import random
import json
import render
from world import World
from entity import Entity


# Functions
def main_loop(world : World, player : Entity):
    entities = [player]
    while True:
        render.print_map(world, entities, player)
        render.clear_line(22)
        user_input = input(">")
        player, world = handle_inputs(user_input, player, world)


def handle_inputs(user_input : str, player : Entity, world : World):
    move_direction = ""
    if user_input == "w":
        move_direction = "up"
    elif user_input == "a":
        move_direction = "left"
    elif user_input == "s":
        move_direction = "down"
    elif user_input == "d":
        move_direction = "right"
    
    if move_direction != "":
        player.move(move_direction, world)
    
    return player, world


# Runs setup for rendering
print("Setting up Rendering")
render.setup()
print(render.set_colour("bright green"))
print("This text should be in green.")
print(render.set_colour("white"))


# Loading
print("Loading Assets")


# Loading Tileset Data
tileset_data = {}
_dir = "Data/Tile Data.json"
with open(_dir, "r") as f:
    tileset_data = json.load(f)


# Loading Ores
ores = {}
_dir = "Data/Ores.json"
with open(_dir, "r") as f:
    ores = json.load(f)


# Loading Entities
entity_data = {}
_dir = "Data/Entities"
for filename in os.listdir(_dir):
    with open(os.path.join(_dir, filename), "r") as f:
        data = json.load(f)
        entity_data[data["name"]] = data


# Initializing World and Player
print("Initializing World")
world = World(1000, 1000, random.randint(1, 10000), tileset_data, ores)
player = Entity(entity_data["human"])
player.x = world.width // 2
while not world.get_tile_data(player.x, player.y + 1)["collides"]:
    player.y += 1


print("Running Main Loop")
main_loop(world, player)

input("Enter to exit...")