from pygame import init


from Colors import *
class Player:
    def __init__(self, color) -> None:
        self.color = color


    def __str__(self) -> str:
        if self.color == RED:
            return "Red"
        else:
            return "Yellow"
        pass