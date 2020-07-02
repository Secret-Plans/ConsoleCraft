from world import World

class Entity:
    x = 0
    y = 0
    visible = False
    moves = False


    def __init__(self, data : dict) -> None:
        if data["visible"]:
            self.visible = True
            self.char = data["char"]
            self.colour = data["colour"]
        if data["moves"]:
            self.moves = True
            self.climbs =  True
            self.falls = True
    

    def move(self, direction : str, amount : int, world : World):
        velocity = [0, 0] #vector2d: x, y
        
        # Evaluate direction
        if direction == "left":
            velocity[0] = -1 * amount
        elif direction == "right":
            velocity[0] = 1 * amount
        elif direction == "up":
            velocity[1] = -1 * amount
        elif direction == "down":
            velocity[1] = 1 * amount
        
        if falls:
            pass