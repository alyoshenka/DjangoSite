import threading
import time

from raylibpy import *

from .window import Window
from .board import Board


def main():

    w = Window()

    b = Board()
    b.def_init_dots()
    w.objs.append(b)

    w.start()

    while not w.open:
        continue
    print('loop:')
    while w.open:

        time.sleep(0.5)
        bo = w.objs[0]
        bo.set_color(0, BLUE)
        w.objs[0] = bo
        print('b: ', w.objs[0].dots[0].color)

        time.sleep(0.5)
        w.objs[0].set_color(0, GREEN)
        print('g: ', w.objs[0].dots[0].color)

if __name__ == '__main__':
    main()