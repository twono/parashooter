import arcade


class Cannon:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def on_draw(self):
        arcade.draw_line(self.x, self.y, self.x, self.y + 50, arcade.color.WHITE, 10)