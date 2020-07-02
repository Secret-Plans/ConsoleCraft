from world import World

class Entity:
    player_controlled = False
    x = 0
    y = 0
    visible = False
    moves = False


    def __init__(self, data : dict, player_controlled : bool = False) -> None:
        self.player_controlled = player_controlled

        if data["visible"]:
            self.visible = True
            self.char = data["char"]
            self.colour = data["colour"]
        if data["moves"]:
            self.moves = True
            self.climbs =  True
            self.falls = True
    

    def move(self, direction : str, world : World) -> None:
        if direction == "left" or direction == "right":
            x = {"left": -1, "right": 1}[direction]
            if not world.does_collide(self.x + x, y):
                self.x += x
            elif self.climbs and self.y > 0:
                if not world.does_collide(self.x + x, self.y - 1):
                    self.x += x
                    self.y -= 1
        elif direction == "up":
            pass
        elif direction == "down":
            pass
    

    def tick(self, world : World) -> None:
        pass