from raylibpy import *


class DisplayBoard():

    def __init__(self, board):

        self.width = board.width
        self.height = board.height
        self.label = board.label
        self.offset = 25

        self.dots = board.leds.all()

        assert(len(self.dots) == self.width * self.height)

    def set_color(self, idx, color):
        self.dots[idx].set_color(color)

    def set_color_RGB(self, idx, r, g, b):
        color = Color(r, g, b, 255)
        set_color(idx, color)
        print(r, ", ", g, ", ", b)
    
    def draw(self):
        try:
            max = len(self.dots)
            for i in range(max):
                x = i // self.height
                y = i % self.height
                led = self.dots.get(index=i)
                my_color = led.color
                ray_color = Color(
                    my_color.r, my_color.g, my_color.b, 255)
                x = x * self.offset + self.offset / 2
                y = y * self.offset + self.offset / 2
                draw_circle(x, y, 5, ray_color)
        except Exception as e:
            print(e)


