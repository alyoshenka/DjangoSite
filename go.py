import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'hubble_site.settings'
import django
django.setup()


from threading import Thread

from leds.RayPy.window import Window
from leds.RayPy.displayBoard import DisplayBoard

from leds.models import Board


win = Window()

dat_board = Board.objects.get(label='display')
disp_board = DisplayBoard(dat_board)
win.objs.append(disp_board)

win.start()

os.system('python manage.py runserver')



