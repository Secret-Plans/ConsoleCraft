

class Entity:
    x = 0
    y = 0
    visible = False


    def __init__(self, data : dict) -> None:
        if data["visible"]:
            self.visible = True
            self.char = data["char"]
            self.colour = data["colour"]