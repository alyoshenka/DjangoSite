import threading

from raylibpy import *


class Window(threading.Thread):
    def __init__(self):
        self.screen_height = 200
        self.screen_width = self.screen_height * 4
        self.open = False
        self.objs = []

        threading.Thread.__init__(self, daemon=True)

    def run(self):
        
        init_window(self.screen_width, self.screen_height, b"RayPy")
        self.open = True

        while not window_should_close():

            begin_drawing()
            clear_background(GRAY)

            self.draw()

            end_drawing()

        close_window()
        self.open = False

    def draw(self):
        for obj in self.objs:
            try:
                obj.draw()
            except:
                print('cannot draw ', obj)