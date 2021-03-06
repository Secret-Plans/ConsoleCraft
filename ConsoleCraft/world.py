import opensimplex
import render
import random

class World:
    width = 10000
    height = 10000
    tiles = [[0]]
    tileset_data = {}
    seed = 0


    def __init__(self, width : int, height : int, seed : int, tileset_data : dict, ore_data : dict) -> None:
        self.width = width
        self.height = height
        self.tileset_data = tileset_data

        self.seed = seed

        self.tiles = [[0] * height for _ in range(width)]


        print("Generating World")
        self.generate(ore_data)
    

    def generate(self, ore_data : dict) -> None:
        # Generate Heightmap and Grass
        print("Generating Heightmap")
        noise = opensimplex.OpenSimplex(self.seed)
        for x in range(self.width):
            render.print_and_back(f"x = {x}")
            y = int(noise.noise2d(x / 10, 1) * 5) + self.height // 2
            while y < self.height - 1:
                self.set_tile(x, y, 1)
                y += 1
        
        # Generate Caves
        print("Generating Caves")
        noise = opensimplex.OpenSimplex(self.seed + 1)
        for x in range(self.width):
            render.print_and_back(f"x = {x}")
            for y in range(0, self.height):
                if noise.noise2d(x / 10, y / 10) > 0.5:
                    if self.get_tile_index(x, y) == 1:
                        self.set_tile(x, y, 2)
        
        # Generate Ores
        print("Generating Ores")
        noise = opensimplex.OpenSimplex(self.seed + 2)
        for x in range(self.width):
            render.print_and_back(f"x = {x}")
            for y in range(self.width):
                if noise.noise2d(x / 10, y / 10) > 0.7:
                    if self.get_tile_index(x, y) == 1:
                        self.set_tile(x, y, 3)
        
        # Generate Grass
        random.seed = self.seed - 1
        for x in range(self.width):
            if random.randint(1, 100) > 50:
                y = 0
                while self.get_tile_index(x, y + 1) == 0:
                    y += 1
                if self.get_tile_index(x, y + 1) == 1:
                    self.set_tile(x, y, 5)


    def get_tile_index(self, x : int, y : int) -> int:
        return self.tiles[x][y]


    def get_tile_data(self, x : int, y : int) -> dict:
        return self.tileset_data[str(self.get_tile_index(x, y))]
    

    def set_tile(self, x : int, y : int, index : int) -> None:
        self.tiles[x][y] = index
    

    def collides(self, x : int, y : int) -> bool:
        return self.get_tile_data(x, y)["collides"]