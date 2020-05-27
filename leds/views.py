from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect

import json

from .models import Color, Board, LED


def index(request):
    """Homepage"""
    board = Board()
    board.default_init()
    arr = board.display_arr()
    all_colors = Color.objects.all()
    try:
        current_color = request.session['current_color']
    except:
        request.session['current_color'] = 'none'
        current_color = 'none'
    context = { 
        'board': board,
        'arr': arr,
        'colors': all_colors,
        'current_color': current_color
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


# session testing

def selected_color(request):
    _label = request.session['current_color']
    color = None if _label == 'none' else Color.objects.get(label=_label)
    return color

def color_click(request, color_label):
    color = Color.objects.get(label=color_label)
    obj = json.loads(color.json())[0]
    label = obj.get('fields').get('label')

    if not 'current_color' in request.session:
        request.session['current_color'] = 'none'
    elif request.session['current_color'] == label:
        request.session['current_color'] = 'none'
    else:
        request.session['current_color'] = label

    # return HttpResponse(request.session['current_color'])
    return HttpResponseRedirect(reverse('leds:index'))

def LED_click(request, led_index):
    # get selected color
    # find associated color by label
    color = selected_color(request)
    if color is not None:
        # find LED associated to button (by idx)
        led = LED.objects.get(index=led_index)
        # set LED color to color
        led.color = color
        # save
        led.save()
    # return to original page   
    return HttpResponseRedirect(reverse('leds:index'))
