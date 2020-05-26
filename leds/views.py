from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect

from .models import Color, Board


def index(request):
    """Homepage"""
    board = Board()
    board.default_init()
    arr = board.display_arr()
    all_colors = Color.objects.all()
    context = { 
        'board': board,
        'arr': arr,
        'colors': all_colors,
     }
    return render(request, 'leds/index.html', context)

def color(request, color_name):
    """Displays information for a given color"""
    color = get_object_or_404(Color, label=color_name)
    context = {
        'color': color
    }
    return render(request, 'leds/color.html', context)

def all_colors(request):
    """Show all the colors"""
    all_colors = Color.objects.all()
    context = {
        'all_colors': all_colors
    }
    return render(request, 'leds/all_colors.html', context)

def set_led_color(request, board_label, led_idx, color_label):

    board = Board.objects.get(label=board_label)
    led = board.leds[led_idx]
    color = Color.objects.get(label=color_label)

    led.color = color
    led.save()

    return HttpResponseRedirect(reverse('leds:boards', args=(board_label,)))
