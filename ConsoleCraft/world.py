

class World:
    width = 10000
    height = 10000
    tiles = [[0]]
    tileset_data = {}


    def __init__(self, width : int, height : int, tileset_data : dict, generation_steps : dict) -> None:
        self.width = width
        self.height = height
        self.tileset_data = tileset_data

        self.tiles = [[0] * height for _ in range(width)]


        print("Generating World")
        self.generate(generation_steps)
    

    def generate(self, steps : dict) -> None:
        for step in steps["terrain"]:
            for y in range(step["start"], step["end"]):
                for x in range(self.width):
                    self.set_tile(x, y, step["tile"])


    def get_tile_index(self, x : int, y : int) -> int:
        return self.tiles[x][y]


    def get_tile_data(self, x : int, y : int) -> dict:
        return self.tileset_data[str(self.get_tile_index(x, y))]
    

    def set_tile(self, x : int, y : int, index : int) -> None:
        self.tiles[x][y] = index