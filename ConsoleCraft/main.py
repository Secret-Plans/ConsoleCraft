# Imports
import os
import json
import render
from world import World
from entity import Entity


# Functions
def main_loop(world):
    entities = []
    while True:
        render.print_map(world, Entity())


# Runs setup for rendering
print("Setting up Rendering")
render.setup()


# Loading
print("Loading Assets")


# Loading Tileset Data
tileset_data = {}
_dir = "Data/Tile Data.json"
with open(_dir, "r") as f:
    tileset_data = json.load(f)


# Loading Generation Steps
generation_steps = {
    "terrain": []
}
_dir = "Data/Generation/Steps"
for filename in os.listdir(_dir):
    with open(os.path.join(_dir, filename), "r") as f:
        data = json.load(f)
        for item in data["root"]:
            if item["type"] == "terrain":
                generation_steps["terrain"].append(item)


# Initializing World and Player
print("Initializing World")
world = World(10000, 10000, tileset_data, generation_steps)

print("Running Main Loop")
main_loop(world)

input("enter to exit...")