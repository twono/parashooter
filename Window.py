import arcade
import Cannon


class Window(arcade.Window):
    def __init__(self):
        super().__init__(800, 600, "Parashooter")
        arcade.set_background_color(arcade.color.BLACK)

        self.cannon = Cannon.Cannon(self.width / 2, 0)

    def on_draw(self):
        arcade.start_render()
        #arcade.draw_circle_filled(400, 300, 100, arcade.color.CORN)

        self.cannon.on_draw()