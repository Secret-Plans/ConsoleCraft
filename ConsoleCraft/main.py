# Imports
import os
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
    if user_input == "w":
        if player.y > 0 and not world.get_tile_data(player.x, player.y - 1)["collides"]:
            player.y -= 1
    elif user_input == "a":
        if player.x > 0 and not world.get_tile_data(player.x - 1, player.y)["collides"]:
            player.x -= 1
    elif user_input == "s":
        if player.y < world.height - 1 and not world.get_tile_data(player.x, player.y + 1)["collides"]:
            player.y += 1
    elif user_input == "d":
        if player.x < world.width - 1 and not world.get_tile_data(player.x + 1, player.y)["collides"]:
            player.x += 1
    elif user_input == "e":
        world.set_tile(player.x, player.y, 1)
    
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


# Loading Entities
entity_data = {}
_dir = "Data/Entities"
for filename in os.listdir(_dir):
    with open(os.path.join(_dir, filename), "r") as f:
        data = json.load(f)
        entity_data[data["name"]] = data


# Initializing World and Player
print("Initializing World")
world = World(2000, 2000, tileset_data)
player = Entity(entity_data["human"])
player.x = world.width // 2
while not world.get_tile_data(player.x, player.y + 1)["collides"]:
    player.y += 1


print("Running Main Loop")
main_loop(world, player)

input("Enter to exit...")